def test_webshop():
    import csv
    import time
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('http://localhost:9999/another_form.html')

    def find_and_clear_by_id(id):
        element = driver.find_element_by_id(id)
        element.clear()
        return element

    with open('c:\\users\\dell\\downloads\\table.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            find_and_clear_by_id('fullname').send_keys(row[0])
            find_and_clear_by_id('email').send_keys(row[1])
            find_and_clear_by_id('dob').send_keys(row[2])
            find_and_clear_by_id('phone').send_keys(row[3])

            driver.find_element_by_id('submit').click()
            time.sleep(2.0)

    link = driver.find_element_by_xpath('//button[text()="Export HTML table to CSV file"]')
    link.click()
    time.sleep(3.0)
    driver.close()

    # with open('table_in.csv', 'r') as t1, open('c:\\users\\dell\\downloads\\table.csv', 'r') as t2:
    #    fileone = t1.readlines()
    #    filetwo = t2.readlines()
    #
    # with open('update.csv', 'w') as outFile:
    #    for line in filetwo:
    #        if line not in fileone:
    #           outFile.write(line)

    with open('c:\\users\\dell\\downloads\\table.csv', 'r') as t1:  # file megnyitas
        t1 = csv.reader(t1)  # atadom valtozonak es beolvasatom
        for row in t1:  # vegig iteral es kiirart
            print(row)
