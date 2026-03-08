


class TestExample:

    def test_url_test(self,setup):
        driver = setup
        actual_url = driver.current_url
        assert actual_url == "https://sauce-demo.myshopify.com/"
        print("url validation passed")

