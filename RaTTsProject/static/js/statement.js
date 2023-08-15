let navbar = document.querySelector('.navbar')

document.querySelector('#menu_btn').onclick = () =>{
    navbar.classList.toggle('active');
    loginForm.classList.remove('active');
    searchForm.classList.remove('active');
}

let userprofile = document.querySelector('.User-Profile')

document.querySelector('#User-Profile').onclick = () =>{
    userprofile.classList.toggle('active');
    navbar.classList.remove('active');
    searchForm.classList.remove('active');
}

let notification = document.querySelector('.User-Notification')

document.querySelector('#User-Notification').onclick = () =>{
    notification.classList.toggle('active');
    navbar.classList.remove('active');
    searchForm.classList.remove('active');
}

async function myfunctionhere(query) {
    try {
      console.log("It does stuff here!")
      let url = "https://www.google.com/search?q=" + query
      console.log("URL: ", url);
      
      return url;
    } catch (error) {
      throw error;
    }
  };
  
  async function secondfunction(doesthings) {
    try {
      console.log("More stuff here in the second function")
      let url = doesthings + " + more words at the end!"
      
      return url;
    } catch (error) {
      throw error;
    }
  };
  
  function searchFunction() {
    let query = document.getElementById('search').value;
    console.log(query);
    query = query.replaceAll(" ", "+");
    
    myfunctionhere(query).then((urls) => {
      console.log("Hey it got through the first function and returned this: ", urls);
      
      secondfunction(urls).then((stuff) => {
        console.log("And also the second, with this! ", stuff);
      });
    });
  };