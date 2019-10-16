from scipy.constants import physical_constants
import re

with open('templates/index.html') as template:
    with open('dist/index.html', 'w') as dist:
        content = template.read()

        units = ""

        seen = set()

        for c in physical_constants:
            identifier = re.sub('[\-\(\) \.\{\}\\\/,]', '_', c, flags=re.M)

            if identifier not in seen:
                seen.add(identifier)
    
                units += "let " + identifier + " = " + str(physical_constants[c][0]) + "\n"

        content = content.replace('{{ units }}', units)
        
        dist.write(content)