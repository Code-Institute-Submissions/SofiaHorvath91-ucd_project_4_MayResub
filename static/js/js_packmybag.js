/* Variables */

/* Constant to pass jQuery for testing with Jest (js_packmybag.test.js), to be commented out in Production */
// const $ = require('jquery');

/* Initialize variables of current bag for pages mybag_add_items / mybag_details */
let currentBagVars = {
    max_bagweight: 0.00,
    current_bagweight: 0.00,
    items_additems: [],
    items_detailsitems: [],
    item: {},
};

/* jQuery */

/* On page load for pages mybag_add_items / mybag_details : pass item list from view to js via json */
$(function () {
    if(window.location.pathname.includes('mybag_add_items')){
        currentBagVars.items_additems = add_items_JSON;
        set_current_max_bagweight(); // If adding items, define possible max bag weight
    }
   if(window.location.pathname.includes('mybag_details')){
        currentBagVars.items_detailsitems = details_items_JSON;
    }
});

/* Calculate bag weight automatically based on the weight of user : 20% of user weight + 1kg (packmybag) */
$(document).on('input', '#userweight', function(){
    get_bagweight_per_userweight($("#userweight").val());
});

/* Handle checking item cb to add to bag : Update bag weight & control max items/max bag weight (mybag_add_items) */
$(".item_checkbox").change(function() {
    var id = this.id;
    var name_page = "";
    if(id.includes("_checked")){
        name_page = "#"+id.split("_")[0];
    } else{
        name_page = "#"+id;
    }
    currentBagVars.item = get_item_from_list(id, currentBagVars.items_additems);
    add_itemweight_to_bagweight(name_page,
                                $(this).prop('checked'),
                                currentBagVars.item.external,
                                currentBagVars.item.weight);
});

/* Handle click on information sign / item name to show item details (mybag_add_items / mybag_details)
=> Source / Inspiration : https://www.w3schools.com/howto/howto_css_modal_images.asp */
$('.info-item').click(function () {
    var id = this.id;
    var name_item = id.split("-")[0];
    var page_name = id.split("-")[2];

    if(page_name == "additems"){
        currentBagVars.item = get_item_from_list(name_item, currentBagVars.items_additems);
    } else{
        currentBagVars.item = get_item_from_list(name_item, currentBagVars.items_detailsitems);
    }
    set_modal_dom_elements_items(currentBagVars.item, page_name);
});

/* Handle click on close icon to close modal (mybag_add_items)*/
$('#additems-close-modal').click(function () {
    onclick_hide_modal($, '#additems-modal');
});

/* Handle click on close icon to close modal (mybag_details)*/
$('#detailsitems-close-modal').click(function () {
    onclick_hide_modal($, '#detailsitems-modal');
});

/* Javascript functions */

/* Get / set max bag weight for current bag & packing upon page load (mybag_add_items) */
function set_current_max_bagweight(){
    var additems_max_bagweight = document.getElementById("additems_max_bag_weight").value;
    currentBagVars.max_bagweight = parseFloat(additems_max_bagweight).toFixed(2);
    var additems_actual_bagweight = document.getElementById("starting_bag_weight").value;
    if(additems_actual_bagweight > 0){
        currentBagVars.current_bagweight = parseFloat(additems_actual_bagweight);
    } else {
        currentBagVars.current_bagweight = currentBagVars.current_bagweight;
    }
    document.getElementById("additems_bag_weight").innerHTML = currentBagVars.current_bagweight + " kg";
}
 /* While defining bag details, calculate automtically bag max weight based on user weight (packmybag) */
function get_bagweight_per_userweight(userweight){
    var bagweight_kg = Math.round(userweight) * 0.2 + 1;
    document.getElementById("bagweight").value = bagweight_kg.toFixed(2);
}

/* Get current item from list of items based on name (mybag_add_items / mybag_details) */
function get_item_from_list(name, list){
   if(name.includes("_checked")){
        return list.find(x => x.name === name.split("_")[0]);
    } else{
        return list.find(x => x.name === name);
    }
}

/* Add/remove current item's weight to/from bag weight upon checkin/unchecking item checkbox
if item cannot be carried externally (out of the bag, in hand or hanged on the bag), update UI DOM element,
and alert/stop user if no more items can be added as max bag weight would be exceeded (mybag_add_items) */
function add_itemweight_to_bagweight(name, checked, external, weight){
    if(!external){
        if(checked){
            currentBagVars.current_bagweight += parseFloat(weight);
            if(currentBagVars.current_bagweight > currentBagVars.max_bagweight){
                alert("You cannot put more items in the bag, remove items before packing new ones.");
                $(name).prop("checked", false);
                currentBagVars.current_bagweight -= parseFloat(weight);
            }
        } else{
            currentBagVars.current_bagweight -= parseFloat(weight);
        }
    }
    document.getElementById("additems_new_bag_weight").value = currentBagVars.current_bagweight.toFixed(2);
    document.getElementById("additems_bag_weight").innerHTML =
    Math.abs(currentBagVars.current_bagweight).toFixed(2) + " kg";
}

/* Show pop-up modal with item details (fields of Item model for current item) when user clicks on name of item
(mybag_add_items / mybag_details) */
function set_modal_dom_elements_items(item, name){
    var link = "http://www.amazon.com/s?url=search-alias%3Daps&field-keywords=";
    if(item.name.includes(" ")){
        var name_list = item.name.split(" ");
        for(var i=0;i<name_list.length;i++){
            if(i < name_list.length - 1){
                link += name_list[i] + "+";
            } else{
                link += name_list[i];
            }
        }
        document.getElementById(name+"_item_amazon_btn").href = link;
    } else{
       document.getElementById(name+"_item_amazon_btn").href = link + item.name;
    }

    document.getElementById(name+"-modal").classList.add("modal-display");

    document.getElementById(name+"_item_name").innerHTML = item.name.toUpperCase();
    document.getElementById(name+"_item_category").innerHTML = "Category : " + item.category;
    document.getElementById(name+"_item_weight").innerHTML = "Average Weight (kg) : " + item.weight;
    var usefulness_item = parseFloat(item.usefulness).toFixed(2);
    document.getElementById(name+"_item_usefulness").innerHTML = "Usefulness : " + usefulness_item + " / 10";
    document.getElementById(name+"_item_external").innerHTML =
    "Can be brought externally (out of bag) : " + (item.external ? "Yes" : "No");

    document.getElementById(name+"_item_with_child").innerHTML =
    "Underage company specific : " + (item.with_child == true ? "Yes" : "No");
    document.getElementById(name+"_item_with_elder").innerHTML =
    "Elder company specific : " + (item.with_elder == true ? "Yes" : "No");
    document.getElementById(name+"_item_with_pet").innerHTML =
    "Pet specific : " + (item.with_pet == true ? "Yes" : "No");

    document.getElementById(name+"_item_climates").innerHTML = "Climates which requires this item :<br>";
    append_list_elements(document.getElementById(name+"_item_climates"), item.climate);
    document.getElementById(name+"_item_landforms").innerHTML = "Landforms which requires this item :<br>";
    append_list_elements(document.getElementById(name+"_item_landforms"), item.landform);
    document.getElementById(name+"_item_environments").innerHTML = "Environments which requires this item :<br>";
    append_list_elements(document.getElementById(name+"_item_environments"), item.environment);

    document.getElementById(name+"_item_available_infrastructure").innerHTML =
    "Human infrastructure : " + (item.available_infrastructure == false ? "Yes" : "No");
    document.getElementById(name+"_item_available_water").innerHTML =
    "Drinking water : " + (item.available_water == false ? "Yes" : "No");
    document.getElementById(name+"_available_food").innerHTML =
    "Comestibles (food) : " + (item.available_food == false ? "Yes" : "No");
}

/* Format list elements into string when having multiple values associated to a field to show in pop-up modal on UI
(mybag_add_items / mybag_details) */
function append_list_elements(dom, list){
    for(var i=0;i<list.length;i++){
        if(i < list.length - 1){
            dom.innerHTML += list[i].name + ", ";
        } else{
            dom.innerHTML += list[i].name;
        }
    }
}

/* Close pop-up modal when clicking on exit sign 'X' (mybag_add_items / mybag_details) */
function onclick_hide_modal($, name){
    $(name).removeClass( 'modal-display' );
}

/* Export modules for testing with Jest (js_packmybag.test.js), to be commented out in Production */

/* module.exports = { currentBagVars,
                   set_current_max_bagweight,
                   get_bagweight_per_userweight,
                   get_item_from_list,
                   add_itemweight_to_bagweight,
                   set_modal_dom_elements_items,
                   append_list_elements,
                   onclick_hide_modal }; */