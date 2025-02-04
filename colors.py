import xml.etree.ElementTree as ET

def read_colors_from_file(filename):
    colors = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                name, color_values = parts
                colors.append((name, color_values))
    return colors

def create_xml(colors, output_file="colors.xml"):
    root = ET.Element("colors", useDefaultColors="true")
    
    for name, color in colors:
        ET.SubElement(root, "color", color=color, name=name)
    
    tree = ET.ElementTree(root)
    with open(output_file, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)
    
    # Pretty-print the XML to ensure each entry is on a separate line
    import xml.dom.minidom
    xml_str = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(xml_str)

def main():
    input_file = "FS25_Colors.txt"
    colors = read_colors_from_file(input_file)
    create_xml(colors)
    print(f"XML file 'colors.xml' created successfully.")

if __name__ == "__main__":
    main()
