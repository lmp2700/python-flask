from lxml import etree


class Address(object):
    def __init__(self, name, address_1, city, state, zipcode, address_2=''):
        self.name = name
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def add_to_xml(self, root, prefix='To', validate=False):
        if not validate:
            name = etree.SubElement(root, prefix + 'Name')
            name.text = self.name
    
        address_1 = etree.SubElement(root, prefix + 'Address1')
        address_1.text = self.address_1

        address_2 = etree.SubElement(root, prefix + 'Address2')
        address_2.text = self.address_2
    
        city = etree.SubElement(root, prefix + 'City')
        city.text = self.city

        state = etree.SubElement(root, prefix + 'State')
        state.text = self.state

        zipcode = etree.SubElement(root, prefix + 'Zip5')
        zipcode.text = self.zipcode