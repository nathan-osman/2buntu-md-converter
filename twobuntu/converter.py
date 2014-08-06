from bs4 import BeautifulSoup
from re import sub


class TwobuntuConverter:
    """
    Convert an article to correctly formatted markdown.
    """

    def convert(self, text):
        """
        Perform conversion on the specified text.

        :param text: the markdown text to convert
        :returns: the converted markdown
        """
        # Create a soup instance
        soup = BeautifulSoup(self._strip_captions(text))

        # Convert <img>, <a>, and <pre> tags
        self._convert_img(soup)
        self._convert_a(soup)
        self._convert_pre(soup)

        # Convert other tags
        self._convert_tags(soup)

        # Remove the body and html tags that BeautifulSoup adds
        soup.body.unwrap()
        soup.html.unwrap()

        return str(soup)

    def _convert_a(self, soup):
        """
        Convert the <a> tags to markdown.

        :param soup: a soup instance
        """
        while soup.find_all('a'):
            a = '[%s](%s)' % (soup.a.string, soup.a['href'])
            soup.a.insert_before(a)
            soup.a.decompose()

    def _convert_img(self, soup):
        """
        Convert the <img> tags to markdown.

        :param soup: a soup instance
        """
        while soup.find_all('img'):
            alt = soup.img['alt'] if 'alt' in soup.img else 'image'
            src = soup.img['src']
            soup.img.insert_before('![%s](%s)' % (alt, src))
            soup.img.decompose()

    def _convert_pre(self, soup):
        """
        Convert the <pre> tags to markdown.

        :param soup: a soup instance
        """
        while soup.find_all('pre'):
            lines = soup.pre.string.splitlines()
            lines = [' ' * 4 + l for l in lines]
            soup.pre.replace_with('\n'.join(lines))

    def _convert_tags(self, soup):
        """
        Convert HTML tags to markdown.

        :param soup: a soup instance
        """
        # Remove Center Tags
        self._modify_text(soup, 'center', '\n', '', 'pre')
        # Remove br Tags
        self._modify_text(soup, 'br', '\n', '', 'pre')
        # Remove hr Tags
        self._modify_text(soup, 'hr', '\n---', '\n', 'prepost')
        # Remove p
        self._modify_text(soup, 'p', '\n', '', 'pre')
        # Remove lists
        self._modify_text(soup, 'ol', '\n', '', 'pre')
        self._modify_text(soup, 'ul', '\n', '', 'pre')
        # Add li markdown -
        self._modify_text(soup, 'li', ' - ', '', 'pre')
        # Add h1-h6 markdown #
        self._modify_text(soup, 'h1', '\n#', '\n', 'prepost')
        self._modify_text(soup, 'h2', '\n##', '\n', 'prepost')
        self._modify_text(soup, 'h3', '\n###', '\n', 'prepost')
        self._modify_text(soup, 'h4', '\n####', '\n', 'prepost')
        self._modify_text(soup, 'h5', '\n#####', '\n', 'prepost')
        self._modify_text(soup, 'h6', '\n######', '\n', 'prepost')
        # Add italics markdown _
        self._modify_text(soup, 'em', '_', '', 'wrap')
        self._modify_text(soup, 'i', '_', '', 'wrap')
        # Add bold markdown **
        self._modify_text(soup, 'strong', '**', '', 'wrap')
        self._modify_text(soup, 'b', '**', '', 'wrap')
        # Add inline code markdown `
        self._modify_text(soup, 'code', '`', '', 'wrap')
        # Remove span tags
        self._modify_text(soup, 'span', '\n', '', 'pre')
        # Remove div tags
        self._modify_text(soup, 'div', '\n', '', 'pre')

    def _find_pre_parent(self, block):
        """
        Determine if one of the parents of block is a <pre>.

        :param block: the block to search
        :returns: true if a <pre> was found
        """
        if hasattr(block, 'parents'):
            return any([p.name == 'pre' for p in block.parents])

    def _strip_captions(self, text):
        """
        Remove [caption] shortcodes.

        :param text: the text to search
        :returns: the text with captions removed
        """
        def process(match):
            tag = BeautifulSoup(match.group(3))
            if tag.find(('a', 'img')):
                return '![image](%s)' % (tag.a['href'] if tag.a else tag.img['src'])
            return ''
        return self._strip_shortcode(text, 'caption', process)

    def _strip_shortcode(self, text, shortcode, callback=None):
        """
        Strips a shortcode from the text.

        :param text: the text to search
        :param shortcode: the shortcode to strip
        :param callack: a callback to process the shortcode
        :returns: the text with the shortcode replaced
        """
        # Default callback for processing which strips tags
        def process(match):
            return match.group(3)
        return sub(
            r'(\[%s(.*?)\](.*?)\[/%s\])' % (shortcode, shortcode),
            callback or process,
            text,
        )

    def _modify_text(self, soup, tag, text1, text2, action):
        """
        Modifies tag to add markup provided by arguments text1 & text2.

        Type of modification is specified by action:
         - pre (use text1 only before),
         - prepost (use text1 before, text2 after),
         - wrap(use text1 before and after)
        """
        while soup.find_all(tag):
            element = soup.find(tag)
            if not self._find_pre_parent(element):
                element.insert_before(text1)
                if action == "wrap":
                    element.insert_after(text1)
                elif action == "prepost":
                    element.insert_after(text2)
                elif action == "pre":
                    pass
                else:
                    return False
                element.unwrap()
            else:
                return False
