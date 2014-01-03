
# Imports ###########################################################

from workbench import scenarios
from workbench.test.selenium_test import SeleniumTest

from .utils import load_scenarios_from_path


# Classes ###########################################################

class MentoringBaseTest(SeleniumTest):

    def setUp(self):
        super(MentoringBaseTest, self).setUp()

        # Use test scenarios
        self.browser.get(self.live_server_url) # Needed to load tests once
        scenarios.SCENARIOS.clear()
        scenarios_list = load_scenarios_from_path('tests/xml')
        for identifier, title, xml in scenarios_list:
            self.addCleanup(scenarios.remove_scenario, identifier)

        # Suzy opens the browser to visit the workbench
        self.browser.get(self.live_server_url)

        # She knows it's the site by the header
        header1 = self.browser.find_element_by_css_selector('h1')
        self.assertEqual(header1.text, 'XBlock scenarios')
