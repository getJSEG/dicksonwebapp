var clickHandler = function()  {
    // nav = document.getElementById("mobile-navigation");
    if ( document.getElementById("mobile-navigation").classList.contains('open') ){
        document.getElementById("mobile-navigation").classList.remove('open');
        document.getElementById("mobile-navigation").classList.add('close');
        document.getElementById("mobile-nav-background").classList.add('background-closed');
        document.getElementById("mobile-nav-background").classList.remove('background-open');

    }else{

        document.getElementById("mobile-navigation").classList.remove('close');
        document.getElementById("mobile-navigation").classList.add('open');
        document.getElementById("mobile-nav-background").classList.add('background-open');
        document.getElementById("mobile-nav-background").classList.remove('background-closed');
    }
};

element = document.getElementById("nav-burger");

element.addEventListener('click', clickHandler, false)
