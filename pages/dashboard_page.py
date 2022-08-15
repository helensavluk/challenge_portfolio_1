from pages.base_page import BasePage


class Dashboard(BasePage):
    Main_page_button_xpath = "//*[text()="Main page"]"
    Players_button_xpath = " //*[text() = "Players"]"
    Language_button_xpath = " //*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span "
    Sign_out_button_xpath = " //*[text() = "Sign out"]"
    Add_player_button_xpath = " //*[@href="/en/players/add"] "
    Dev_team_contact_xpath = " //*[@href="https://app.slack.com/client/T3X4CAKNU/C3XTEGXB6"] "
    Logo_scouts_panel_img_xpath = " //*[@title = "Logo Scouts Panel"]"
    Last_updated_report_link_xpath = " //*[@href="/en/players/6026b48956c79737b3f3c624/reports/605a2740d6f567200510a7d6/edit"]"
    Matches_count_box_xpath = " //*[div="Matches count"] "
    Matches_count_number_xpath = " //*[div="Matches count"]/child::div[2] "
    Logo_scouts_panel_img_xpath = " //*[@class='MuiCardMedia-root jss8'] "

pass