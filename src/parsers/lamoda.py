import httpx
from bs4 import BeautifulSoup

from src.services import controller


class LamodaParser:
    @staticmethod
    def parse_product_list(base_url: str) -> None:
        page_num = 1
        is_empty = False

        while is_empty is False:
            url = base_url.format(page_num)
            page_num += 1
            content = httpx.get(url).text
            soup = BeautifulSoup(content, "html.parser")
            product_list = soup.find_all("div", class_="x-product-card__card")

            if not product_list:
                is_empty = True

            else:
                gender = soup.find("a", class_="d-header-genders_link_active").text
                category = soup.find("div", class_="x-footer-seo-menu-tab_opened").text

                for product in product_list:
                    full_price = product.find(
                        "span",
                        "x-product-card-description__price-WEB8507_price_no_bold",
                    ).text.strip()
                    price, currency = full_price[:-3], full_price[-2:]
                    brand = product.find(
                        "div", "x-product-card-description__brand-name"
                    ).text
                    product_name = product.find(
                        "div", "x-product-card-description__product-name"
                    ).text
                    link = product.find(
                        "a", "x-product-card__link x-product-card__hit-area"
                    )["href"]

                    data = {
                        "brand": brand,
                        "product": product_name,
                        "price": price,
                        "currency": currency,
                        "gender": gender,
                        "category": category,
                        "url": link,
                    }
                    controller.lamoda.create_product(data=data)
