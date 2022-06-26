function myFunction() {

    fetch('https://reqres.in/api/users').then(
        response => response.json()
    ).then(
        responseOBJECT => createUsersList(responseOBJECT.data)
    ).catch(
        err => console.log(err)
    )
}

function createUsersList(users) {
    console.log(users);
    const user = users[0];
    const id = document.getElementById("user_id_ins").value;
    const curr_main = document.querySelector("main");
    let i = 0;
    curr_main.innerHTML="";
    for (let user of users) {
        console.log(user);
        i += 1;
        const section = document.createElement('section');

        if (id == i) {
            section.innerHTML = `<img src="${user.avatar}" alt="Profile Picture"/><br>
                                 <div>
                                     <h4>${user.first_name} ${user.last_name}</h4>
                                     <h4>${user.email}</h4><br>
                                 </div>`;
            curr_main.appendChild(section);
        }

    }
}