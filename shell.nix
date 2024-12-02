{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
buildInputs = [
    python3
    postgresql
    # dev dependencies, not needed on prod env
    pipenv
    pre-commit
    git
    ruff
];

shellHook = ''

# Read .env file
source .env

export LOCALE_ARCHIVE="${pkgs.glibcLocales}/lib/locale/locale-archive"
export PGDATA=$PWD/.postgres/db/postgres_data
export PGHOST=$PWD/.postgres/db/postgres
export PGPORT=$DB_PORT
export LOG_PATH=$PWD/.postgres/db/postgres/LOG
export DATABASE_URL="postgresql:///$DB_USER?host=$PGHOST&port=$PGPORT"
export LC_ALL="en_GB.UTF-8"
export LC_MESSAGES="en_GB.UTF-8"
echo $HOSTNAME

# fixes libstdc++ issues and libgl.so issues
LD_LIBRARY_PATH=${stdenv.cc.cc.lib}/lib/:/run/opengl-driver/lib/

# Create directory if need be
if [ ! -d $PGHOST ]; then
mkdir -p $PGHOST
fi
if [ ! -d $PGDATA ]; then
echo 'Initializing postgresql database...'
initdb $PGDATA --auth=trust >/dev/null
fi

pg_ctl restart -l $LOG_PATH -o "-c unix_socket_directories=$PGHOST"
createuser $DB_USER --superuser --createdb

# Create user and database if need be
psql -U $DB_USER -tc "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME'" | grep -q 1 || psql -U $DB_USER -c "CREATE DATABASE $DB_NAME"

unset NODE_OPTIONS

# Installing python packages
set -h #remove "bash: hash: hashing disabled" warning !
SOURCE_DATE_EPOCH=$(date +%s)
export LD_LIBRARY_PATH="${lib.makeLibraryPath [ zlib stdenv.cc.cc ]}":LD_LIBRARY_PATH;
eval "$extras"

if ! [ -d venv ]; then
    python -m venv venv
fi

source venv/bin/activate

python -m pip install --cache-dir=$TMPDIR --upgrade pip

export TMPDIR=/tmp
unset NODE_OPTIONS

if [ -e requirements.txt ]; then
    pip install --cache-dir=$TMPDIR -r requirements.txt
    pip uninstall ruff
fi

python manage.py migrate

'';
}
