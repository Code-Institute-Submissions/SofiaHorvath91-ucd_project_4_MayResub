/**
 * @jest-environment jsdom
 */
require('jest-fetch-mock').enableMocks()

/* Initialize jQuery */
const $ = require('jquery');

/* Modules exported from js_packmybag.js */
const {currentBagVars,
       set_current_max_bagweight,
       get_bagweight_per_userweight,
       get_item_from_list,
       add_itemweight_to_bagweight,
       set_modal_dom_elements_items,
       append_list_elements,
       onclick_hide_modal} = require("./js_packmybag");

/* Set up test objects and test UI */
beforeAll(() => {
    climate_dry = { name:'Dry' };
    climate_tropical = { name:'Tropical' };
    climate_continental = { name:'Continental' };
    climate_temperate = { name:'Temperate' };
    climate_polar = { name:'Polar' };

    item1 = {
        name:'rope', category:'Safety',
        weight:1, usefulness:8,
        climate:'Continental', landform:'Mountains', environment:'Forest',
        external:true, with_child:false, with_pet:true, with_elder:false,
        available_infrastructure:false, available_water:true, available_food:null,
    };
    item2 = {
        name:'radio', category:'Communication',
        weight:0.5, usefulness:9,
        climate:'Continental', landform:'Mountains', environment:'Forest',
        external:false, with_child:true, with_pet:false, with_elder:false,
        available_infrastructure:false, available_water:null, available_food:null,
    };
    item3 = {
        name:'soap', category:'Hygiene',
        weight:0.1, usefulness:7,
        climate:'Continental', landform:'Mountains', environment:'Forest',
        external:false, with_child:true, with_pet:true, with_elder:true,
        available_infrastructure:null, available_water:false, available_food:true,
    };

    document.body.innerHTML =
    "<span id='additems-close-modal' class='close-modal'>"
    + "<h4 id='additems_bag_weight'></h4>"
    + "<input type='number' id='bagweight' name='bagweight' readonly/>"
    + "<input type='hidden' id='additems_new_bag_weight' name='additems_new_bag_weight'>"
    + "<input type='hidden' id='additems_max_bag_weight'>"
    + "<input type='hidden' id='starting_bag_weight'>"
    + "<div id='additems-modal'></div>"
    + "<h3 class='text-center' id='additems_item_name'></h3>"
    + "<a class='btn btn-lg btn-warning text-center' id='additems_item_amazon_btn'></a>"
    + "<label class='modal-label mb-2' id='additems_item_category'></label>"
    + "<label class='modal-label mb-2' id='additems_item_weight'></label>"
    + "<label class='modal-label mb-2' id='additems_item_usefulness'></label>"
    + "<label class='modal-label mb-2' id='additems_item_external'></label>"
    + "<label class='modal-label mb-2' id='additems_item_with_child'></label>"
    + "<label class='modal-label mb-2' id='additems_item_with_elder'></label>"
    + "<label class='modal-label mb-2' id='additems_item_with_pet'></label>"
    + "<label class='modal-label mb-2' id='additems_item_climates'></label>"
    + "<label class='modal-label mb-2' id='additems_item_landforms'></label>"
    + "<label class='modal-label mb-2' id='additems_item_environments'></label>"
    + "<label class='modal-label mb-2' id='additems_item_available_infrastructure'></label>"
    + "<label class='modal-label mb-2' id='additems_item_available_water'></label>"
    + "<label class='modal-label mb-2' id='additems_available_food'></label>";
});

/* Test function 'set_current_max_bagweight' */
describe("Current and max bag weight calculated/shown correctly upon loading page for adding items", () => {
    beforeAll(() => {
        document.getElementById("additems_max_bag_weight").value = 13;
        document.getElementById("starting_bag_weight").value = 0;
        currentBagVars.current_bagweight = 5.3;
        set_current_max_bagweight();
    });
    test("Display current bag weight", () => {
        expect(document.getElementById("additems_bag_weight").innerHTML).toEqual("5.3 kg");
    });
    test("Calculate maximum bag weight", () => {
        expect(currentBagVars.max_bagweight).toBe("13.00");
    });
});

/* Test function 'get_bagweight_per_userweight' */
describe("Current bag weight calculated based on user weight", () => {
    beforeAll(() => {
        userweight = 56; // 56 * 20% = 11.2 + 1 = 12.2
        get_bagweight_per_userweight(userweight);
    });
    test("Display current bag weight : 20% of user's weight + 1kg", () => {
        expect(document.getElementById("bagweight").value).toEqual("12.20");
    });
});

/* Test function 'get_item_from_list' */
describe("Select item from list based on name", () => {
    beforeAll(() => {
        name="rope";
        list = [item3,item1,item2];
        item = get_item_from_list(name, list);
    });
    test("Verify selected item's name (positive scenario)", () => {
        expect(item.name).toBe("rope");
    });
    test("Verify selected item's name (negative scenario)", () => {
        expect(item.name).not.toBe("radio");
    });
});

/* Test function 'add_itemweight_to_bagweight' */
describe("Add/remove current item's weight to/from bag weight with respected max bag weight (not external)", () => {
    beforeAll(() => {
        currentBagVars.current_bagweight = 9.2;
        currentBagVars.max_bagweight = 10
        name="#radio";
        add_itemweight_to_bagweight(name, true, item2.external, item2.weight) // weight=0.5 / external=false
    });
    test("Verify update of bag's current weight", () => {
        expect(currentBagVars.current_bagweight).toBe(9.7);
    });
    test("Verify if bag's current weight < bag's max weight (positive scenario)", () => {
        expect(currentBagVars.current_bagweight).toBeLessThanOrEqual(currentBagVars.max_bagweight);
    });
    test("Verify if bag's current weight > bag's max weight (negative scenario)", () => {
        expect(currentBagVars.current_bagweight).not.toBeGreaterThan(currentBagVars.max_bagweight);
    });
    test("Verify update of bag's current weight on UI", () => {
        expect(document.getElementById("additems_bag_weight").innerHTML).toEqual("9.70 kg");
    });
    test("Verify update of bag's new weight based on current weight in hidden input to pass to Django view", () => {
        expect(document.getElementById("additems_new_bag_weight").value).toEqual("9.70");
    });
});

/* Test function 'add_itemweight_to_bagweight' */
describe("Add/remove current item's weight to/from bag weight with exceeded max bag weight (not external)", () => {
    beforeAll(() => {
        currentBagVars.current_bagweight = 9.7;
        currentBagVars.max_bagweight = 10
        name="#radio";
        add_itemweight_to_bagweight(name, true, item2.external, item2.weight) // weight=0.5 / external=false
    });
    test("Verify that bag's current weight is not updated", () => {
        expect(currentBagVars.current_bagweight).toBe(9.7);
    });
    test("Verify if bag's current weight not bigger than bag's max weight: no update happened as max exceeded", () => {
        expect(currentBagVars.current_bagweight).not.toBeGreaterThan(currentBagVars.max_bagweight);
    });
    test("Verify that bag's current weight is not updated on UI", () => {
        expect(document.getElementById("additems_bag_weight").innerHTML).toEqual("9.70 kg");
    });
    test("Verify that update of bag's new weight based on current weight in hidden input not executed", () => {
        expect(document.getElementById("additems_new_bag_weight").value).toEqual("9.70");
    });
});

/* Test function 'add_itemweight_to_bagweight' */
describe("Add/remove current item's weight to/from bag weight with respected max bag weight (external)", () => {
    beforeAll(() => {
        currentBagVars.current_bagweight = 9.7;
        currentBagVars.max_bagweight = 10
        name="#rope";
        add_itemweight_to_bagweight(name, true, item1.external, item1.weight) // weight=1 / external=true
    });
    test("Verify that bag's current weight is not updated (as external)", () => {
        expect(currentBagVars.current_bagweight).toBe(9.7);
    });
    test("Verify if bag's current weight not bigger than bag's max weight: no update happened (as external)", () => {
        expect(currentBagVars.current_bagweight).not.toBeGreaterThan(currentBagVars.max_bagweight);
    });
    test("Verify that bag's current weight is not updated on UI (as external)", () => {
        expect(document.getElementById("additems_bag_weight").innerHTML).toEqual("9.70 kg");
    });
    test("Verify that no update of bag's new weight as per current weight in hidden input (as external)", () => {
        expect(document.getElementById("additems_new_bag_weight").value).toEqual("9.70");
    });
});

/* Test function 'set_modal_dom_elements_items' */
describe("Current item details shows correctly in pop-up modal", () => {
    beforeAll(() => {
        currentBagVars.item = item1;
        name = "additems";
        set_modal_dom_elements_items(currentBagVars.item, name);
    });
    test("Class for display in block added to DOM", () => {
        expect(document.getElementById("additems-modal").classList.contains('modal-display')).toBe(true)
    });
    test("Display item name in uppercase", () => {
        expect(document.getElementById(name+"_item_name").innerHTML)
        .toEqual("ROPE");
    });
    test("Display item name not is lowercase", () => {
        expect(document.getElementById(name+"_item_name").innerHTML)
        .not.toEqual("rope");
    });
    test("Dispay Amazon link with current item name", () => {
        expect(document.getElementById(name+"_item_amazon_btn").href)
        .toEqual("http://www.amazon.com/s?url=search-alias%3Daps&field-keywords=rope");
    });
    test("Display number value with two decimals", () => {
        expect(document.getElementById(name+"_item_usefulness").innerHTML)
        .toEqual("Usefulness : 8.00 / 10");
    });
    test("Display text / boolean value when for true, the text should be Yes (defined by ternary operation)", () => {
        expect(document.getElementById(name+"_item_external").innerHTML)
        .toEqual("Can be brought externally (out of bag) : Yes");
    });
    test("Display text / boolean value for item when for true, the text should be No", () => {
        expect(document.getElementById(name+"_item_available_water").innerHTML)
        .toEqual("Drinking water : No");
    });
    test("Display text / boolean value for item when for null, the text should be No", () => {
        expect(document.getElementById(name+"_available_food").innerHTML)
        .toEqual("Comestibles (food) : No");
    });
    test("Display text / boolean value for item when for false, the text should be Yes", () => {
        expect(document.getElementById(name+"_item_available_infrastructure").innerHTML)
        .toEqual("Human infrastructure : Yes");
    });
    test("Display text / boolean value for item when for true, the text should be Yes", () => {
        expect(document.getElementById(name+"_item_with_pet").innerHTML)
        .toEqual("Pet specific : Yes");
    });
    test("Display text / boolean value for item when for false, the text should be No", () => {
        expect(document.getElementById(name+"_item_with_child").innerHTML)
        .toEqual("Underage company specific : No");
    });
});

/* Test function 'append_list_elements' */
describe("Add items from list to dom element separated by comma except last item", () => {
    beforeAll(() => {
        dom = document.getElementById("additems_item_climates");
        list = [climate_dry,climate_tropical,climate_continental,climate_temperate,climate_polar];
        append_list_elements(dom, list);
    });
    test("Display list items separated by comma except last item", () => {
        expect(document.getElementById("additems_item_climates").innerHTML)
        .toEqual("Climates which requires this item :<br>undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefinedDry, Tropical, Continental, Temperate, Polar");
        // undefined values included for chanining strings in javascript code (line 129-130)
    });
});

/* Test event 'onclick_hide_modal' (jQuery) */
describe( 'Hide modal on click of exist sign', () => {
	const addClass = jest.fn();
	const removeClass = jest.fn();

	const jQuery = jest.fn(() => ({
        addClass,
        removeClass,
	}));

	it( 'Removes class when has class to display added', () => {
		onclick_hide_modal(jQuery);
        expect(addClass.mock.calls.length).toBe(0);
		expect(removeClass.mock.calls.length).toBe(1);
	});
});