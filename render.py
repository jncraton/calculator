with open('templates/index.html') as template:
    with open('dist/index.html', 'w') as dist:
        content = template.read()

        content = content.replace('{{ units }}', 'let speed_of_light = 3e8')
        
        dist.write(content)