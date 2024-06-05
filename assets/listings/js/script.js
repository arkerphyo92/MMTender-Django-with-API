const sidebarToggle = document.querySelector("#sidebar-toggle");
sidebarToggle.addEventListener("click",function(){
    document.querySelector("#sidebar").classList.toggle("collapsed");
});



function toggleRootClass(){
    const current = document.documentElement.getAttribute('data-bs-theme');
    const inverted = current == 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-bs-theme',inverted);
}

function toggleLocalStorage(){
    if(isLight()){
        localStorage.removeItem("light");
    }else{
        localStorage.setItem("light","set");
    }
}

function isLight(){
    return localStorage.getItem("light");
}

if(isLight()){
    toggleRootClass();
}

document.addEventListener('DOMContentLoaded', function () {
    const ministryField = document.getElementById('id_source_ministry');
    const departmentField = document.getElementById('id_department');
    const locationField = document.getElementById('id_location');
    const cityField = document.getElementById('id_city');

    ministryField.addEventListener('change', function () {
        const ministryId = ministryField.value;
        if (ministryId) {
            fetch(`/api/departments/${ministryId}/`)
                .then(response => response.json())
                .then(data => {
                    departmentField.innerHTML = '';
                    data.forEach(department => {
                        const option = document.createElement('option');
                        option.value = department.id;
                        option.textContent = department.name;
                        departmentField.appendChild(option);
                    });
                });
        }
    });

    locationField.addEventListener('change', function () {
        const locationId = locationField.value;
        if (locationId) {
            fetch(`/api/cities/${locationId}/`)
                .then(response => response.json())
                .then(data => {
                    cityField.innerHTML = '';
                    data.forEach(city => {
                        const option = document.createElement('option');
                        option.value = city.id;
                        option.textContent = city.name;
                        cityField.appendChild(option);
                    });
                });
        }else {
            cityField.innerHTML = '<option value="">---------</option>';
        }
    });
});