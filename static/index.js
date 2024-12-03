


window.onload = async () => {
    let imgBaseUrl = 'static/img/';//FIXME

    let showDialog = false;

    let btn = document.getElementById('menuCantina');
    let dialog = document.getElementById('dialog');
    let entreePlat = document.getElementById('entreePlat');
    let platPlat = document.getElementById('platPlat');
    let dessertPlat = document.getElementById('dessertPlat');
    let close = document.getElementById('close');


    const setMenu = (menu) => {
        let starters = [];
        let mains = [];
        let desserts = [];

        for (let plat of menu.recipes) {
            if (plat.type_plat === 'starter') {
                starters.push(plat);
            } else if (plat.type_plat === 'main') {
                mains.push(plat);
            } else if (plat.type_plat === 'dessert') {
                desserts.push(plat);
            }
        }

        entreePlat.innerHTML = '';
        platPlat.innerHTML = '';
        dessertPlat.innerHTML = '';

        let createElementsFromPlat = (plat) => {
            let container = document.createElement('div');
            container.className = '';

            let title = document.createElement('div');
            container.appendChild(title);
            title.innerHTML = plat.name;
            title.className = '';

            let scores = document.createElement('div');
            container.appendChild(scores);
            scores.className = 'scoreIcons';

            let url = '';
            if (plat.nutriscore === 'a') {
                url = `${imgBaseUrl}Nutri-score-A.svg`;
            } else if (plat.nutriscore === 'b') {
                url = `${imgBaseUrl}Nutri-score-B.svg`;
            } else if (plat.nutriscore === 'c') {
                url = `${imgBaseUrl}Nutri-score-C.svg`;
            } else if (plat.nutriscore === 'd') {
                url = `${imgBaseUrl}Nutri-score-D.svg`;
            } else {
                url = `${imgBaseUrl}Nutri-score-E.svg`;
            }

            let nutriscore = document.createElement('img');
            scores.appendChild(nutriscore);
            nutriscore.src = url;
            nutriscore.className = 'scoreIcon';

            let ecoscore = document.createElement('div');
            scores.appendChild(ecoscore);
            ecoscore.className = 'scoreIcon';

            let ecoscoreImg = document.createElement('img');
            ecoscore.appendChild(ecoscoreImg);
            ecoscoreImg.src = `${imgBaseUrl}coût environnemental.jpg`;
            ecoscoreImg.className = 'scoreImg';

            let ecoscoreText = document.createElement('div');
            ecoscore.appendChild(ecoscoreText);
            ecoscoreText.className = 'scoreText';
            ecoscoreText.innerHTML = plat.cs;

            if (!plat.is_bio) {
                let advertise = document.createElement('div');
                container.appendChild(advertise);
                advertise.innerHTML = 'Coût environnemental pour la même recette en bio : 100 pts';
                advertise.className = 'advertise';
            } else {
                let bio = document.createElement('img');
                scores.appendChild(bio);
                bio.src = `${imgBaseUrl}AB_logo.svg`;
                bio.className = 'scoreIconBio';
            }


            return container;
        };
        for (let starter of starters) {
            let container = createElementsFromPlat(starter);
            entreePlat.appendChild(container);
        }

        for (let main of mains) {
            let container = createElementsFromPlat(main);
            platPlat.appendChild(container);
        }

        for (let dessert of desserts) {
            let container = createElementsFromPlat(dessert);
            dessertPlat.appendChild(container);
        }
    };

    btn.onclick = () => {
        showDialog = !showDialog;
        if (showDialog) {
            dialog.className = "dialog show";
        } else {
            dialog.className = "dialog";
        }
    }

    close.onclick = () => {
        showDialog = false;
        dialog.className = "dialog";
    }

    // let menu = { "name": "Méditerranéen", "recipes": [{ "name": "Salade d'aubergines grillées et mozzarella", "type_plat": "starter", "cs": 1234.5, "nutriscore": "c", "is_bio": false }, { "name": "Colin grillé, légumes vapeur et riz basmati", "type_plat": "main", "cs": 1111, "nutriscore": "b", "is_bio": false }, { "name": "Salade de fruits frais", "type_plat": "dessert", "cs": 13, "nutriscore": "a", "is_bio": true }] };
    // setMenu(menu);

    const response = await fetch('api/recette');
    if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
    } else {
        const json = await response.json();
        setMenu(json);
    }
};