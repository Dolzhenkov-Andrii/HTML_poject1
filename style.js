 const headerBOX = document.querySelector("header");
 const nigthStyleBox = [
    document.querySelector("body"),
    document.querySelector(".features_item"),
    document.querySelector(".intro_features_text"),
 ];

 function dark_on_or_off(){
  if(localStorage.getItem("dark_style") === "dark_on"){
    for (let my_class_key of nigthStyleBox){
        if (my_class_key != null){
            my_class_key.classList.add("the_night");
        }
    }
  } else {
    for (let my_class_key of nigthStyleBox){
        if (my_class_key != null){
            my_class_key.classList.remove("the_night");
        }
    }
  }
 }   
 dark_on_or_off();
 
document.querySelector(".day_night").addEventListener("click", function(){
    if(localStorage.getItem("dark_style") === "dark_on"){
        localStorage.removeItem("dark_style");
    } else {
        localStorage.setItem("dark_style", "dark_on");
    }
    dark_on_or_off();
});

