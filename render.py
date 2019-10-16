with open('templates/index.html') as template:
    with open('dist/index.html', 'w') as dist:
        dist.write(template.read())