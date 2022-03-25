/**
 * @jest-environment jsdom
 */

const $ = require('jquery');
const { currentBagVars, set_dom_current_bag_weight } = require("./js_packmybag");

beforeAll(() => {
    document.body.innerHTML = "<h4 id='additems_bag_weight'></h4>";
});

describe("Current bag weight shows correctly upon adding items to bag", () => {
    beforeAll(() => {
        currentBagVars.current_bagweight = 12;
        set_dom_current_bag_weight();
    });
    test("should display current bag weight with 2 decimals", () => {
        expect(document.getElementById("additems_bag_weight").innerHTML).toEqual("12.00 kg");
    });
});

