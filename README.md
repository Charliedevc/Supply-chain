START
Initialize inventory as empty dictionary

FUNCTION add_product(id, name, stock, reorder_level)
    Add product details to inventory with given stock and reorder level

FUNCTION update_stock(id, quantity_change)
    IF id exists in inventory THEN
        Update stock by adding quantity_change (positive or negative)
        IF stock < reorder_level THEN
            PRINT alert: "Stock low for product [name]"
        ENDIF
    ELSE
        PRINT "Product not found"
    ENDIF

FUNCTION print_inventory_report()
    FOR each product in inventory
        PRINT product ID, name, stock, reorder alert if applicable

MAIN LOOP
    Show menu: Add product, Update stock, Print report, Exit
    GET user choice
    IF Add product THEN
        Prompt for product info and call add_product()
    ELSE IF Update stock THEN
        Prompt for product ID and quantity and call update_stock()
    ELSE IF Print report THEN
        Call print_inventory_report()
    ELSE IF Exit THEN
        STOP
    ENDIF
END
