w, h = 1080, 1080

plates = [["#69d2e7","#a7dbd8","#e0e4cc","#f38630","#fa6900"],["#fe4365","#fc9d9a","#f9cdad","#c8c8a9","#83af9b"],["#ecd078","#d95b43","#c02942","#542437","#53777a"],["#556270","#4ecdc4","#c7f464","#ff6b6b","#c44d58"],["#774f38","#e08e79","#f1d4af","#ece5ce","#c5e0dc"],["#e8ddcb","#cdb380","#036564","#033649","#031634"],["#490a3d","#bd1550","#e97f02","#f8ca00","#8a9b0f"],["#594f4f","#547980","#45ada8","#9de0ad","#e5fcc2"],["#00a0b0","#6a4a3c","#cc333f","#eb6841","#edc951"],["#e94e77","#d68189","#c6a49a","#c6e5d9","#f4ead5"],["#3fb8af","#7fc7af","#dad8a7","#ff9e9d","#ff3d7f"],["#d9ceb2","#948c75","#d5ded9","#7a6a53","#99b2b7"],["#ffffff","#cbe86b","#f2e9e1","#1c140d","#cbe86b"],["#343838","#005f6b","#008c9e","#00b4cc","#00dffc"],["#efffcd","#dce9be","#555152","#2e2633","#99173c"],["#413e4a","#73626e","#b38184","#f0b49e","#f7e4be"],["#ff4e50","#fc913a","#f9d423","#ede574","#e1f5c4"],["#99b898","#fecea8","#ff847c","#e84a5f","#2a363b"],["#655643","#80bca3","#f6f7bd","#e6ac27","#bf4d28"],["#00a8c6","#40c0cb","#f9f2e7","#aee239","#8fbe00"],["#351330","#424254","#64908a","#e8caa4","#cc2a41"],["#554236","#f77825","#d3ce3d","#f1efa5","#60b99a"],["#5d4157","#838689","#a8caba","#cad7b2","#ebe3aa"],["#fad089","#ff9c5b","#f5634a","#ed303c","#3b8183"],["#8c2318","#5e8c6a","#88a65e","#bfb35a","#f2c45a"],["#f8b195","#f67280","#c06c84","#6c5b7b","#355c7d"],["#ff4242","#f4fad2","#d4ee5e","#e1edb9","#f0f2eb"],["#d1e751","#ffffff","#000000","#4dbce9","#26ade4"],["#1b676b","#519548","#88c425","#bef202","#eafde6"],["#5e412f","#fcebb6","#78c0a8","#f07818","#f0a830"]]
selected_plates = int(random(len(plates)))

# Rotate around the center and draw spaced out line sections to the edges
def circle_one(x, y, r):

    max_section_length = r/30
    section_spacing = 10
    translate(x, y)
    strokeWeight(5)


    for i in range(360):
        rotate(radians(1))

        current_point = [0, 0]
        end_point = [0, current_point[1] + int(random(0, max_section_length))]
        while (end_point[1] + section_spacing < r/2):

            line(current_point[0], current_point[1], end_point[0], end_point[1])
            colorIndex =  int(random(len(plates[selected_plates])))
            useColor= plates[selected_plates][colorIndex]
            stroke(useColor)
            current_point = [0, end_point[1] + section_spacing]
            end_point = [0, current_point[1] + int(random(0, max_section_length))]

        line(current_point[0], current_point[1], current_point[0], r/2)


# Pure Random Walk (added parameter for depth in case of recursion)
def circle_four(x, y, r, d):
    pushMatrix()
    translate(x, y)
    noFill()
    stroke(0, 15)
    colorIndex =  int(random(len(plates[selected_plates])))
    useColor= plates[selected_plates][colorIndex]
    stroke(useColor)
    steps = [-1, 1]
    rotate(random(2*PI))
    current_point = [0, r/2.2]
    if (d < 50):
        while(distance(current_point, (0, 0)) < r/2):
            point(current_point[0], current_point[1])

            current_point[0] += random(-1, 1)
            current_point[1] += random(-1, 1)
    else:
        return

    popMatrix()
    circle_four(x, y, r, d + 1)

# Directed random walk
def circle_five(x, y, r, d):
    pushMatrix()
    translate(x, y)
    noFill()
    stroke(0, 255)
    colorIndex =  int(random(len(plates[selected_plates])))
    useColor= plates[selected_plates][colorIndex]
    stroke(useColor)
    steps = [-4, 4, 0, 0]
    rotate(random(2*PI))
    current_point = [0, 0]
    if (d < 100):
        while(distance(current_point, (0, 0)) < r/2):
            point(current_point[0], current_point[1])

            current_point[0] += steps[int(random(len(steps)))]
            if (current_point[0] != 0):
                current_point[1] += steps[int(random(len(steps) - 2))]
    else:
        return

    popMatrix()
    circle_five(x, y, r, d + 1)

# Directed random walk with lines
def circle_six(x, y, r, d):
    pushMatrix()
    translate(x, y)
    noFill()
    stroke(0, 255)
    steps = [-7, 7, 0, 0]
    rotate(random(2*PI))
    current_point = [0, 0]
    last_point = current_point[:]
    colorIndex =  int(random(len(plates[selected_plates])))
    useColor= plates[selected_plates][colorIndex]
    stroke(useColor)
    if (d < 100):
        while(distance(current_point, (0, 0)) < r/2):
            current_point[0] += steps[int(random(len(steps)))]
            if (current_point[0] != 0):
                current_point[1] += steps[int(random(len(steps) - 2))]

            line(current_point[0], current_point[1], last_point[0], last_point[1])

            last_point = current_point[:]
    else:
        return

    popMatrix()
    circle_six(x, y, r, d + 1)

def circle_seven(x, y, r):
    translate(x, y)
    noFill()

    arc_count = 200

    for i in range(arc_count):
        strokeWeight(random(2, 3))
        colorIndex =  int(random(len(plates[selected_plates])))
        useColor= plates[selected_plates][colorIndex]
        stroke(useColor)
        rotate(random(2*PI))
        a = random(r)
        arc(0, 0, a, a, 0, PI)

# Create a base deformed circle and then iterate off of it
def circle_eight(x, y, r):
    translate(x, y)
    noFill()
    strokeWeight(4)

    points = []
    for i in range(0, 360, 15):
        points.append((r/2*sin(radians(i)), r/2*cos(radians(i))))

    # Create the base
    final = []
    for p in points:
        x_change = p[0] / 55.0
        y_change = p[1] / 55.0

        change = random(-3, 3)
        p = (p[0] + x_change * change, p[1] + y_change * change)
        final.append(p)


    for i in range(8):
        variation = []
        for p in final:
            colorIndex =  int(random(len(plates[selected_plates])))
            useColor= plates[selected_plates][colorIndex]
            stroke(useColor)
            x_change = p[0] / 55.0
            y_change = p[1] / 55.0

            change = random(-2, 5)
            p = (p[0] + x_change * change, p[1] + y_change * change)
            variation.append(p)

        beginShape()
        for p in variation:
            curveVertex(*p)
        curveVertex(*variation[0])
        curveVertex(*variation[1])
        curveVertex(*variation[2])
        endShape()


def draw_line(p, v, l, d, md, r):
    if (d > md):
        return

    start_point = p[:]
    end_point = (p[0] + v[0] * l, p[1] + v[1] * l)

    if (distance(end_point, (0, 0)) > r/2):
        draw_line(start_point, v, l*.3, d, md, r)


    if (distance(end_point, (0, 0)) > r/2):
        return

    #line(start_point[0], start_point[1], end_point[0], end_point[1])
    strokeWeight(2)
    lr = -40
    hr = 40
    curve(start_point[0] + random(lr, hr), start_point[1] + random(lr, hr), start_point[0], start_point[1], end_point[0], end_point[1], end_point[0] + random(lr, hr), end_point[1] + random(lr, hr))

    if (random(1) < 1):
        v_one = v.copy()
        v_one.rotate(random(0, .16) * PI)
        draw_line(end_point, v_one, l, d + 1, md, r)

    if (random(1) < 1):
        v_two = v.copy()
        v_two.rotate(random(1.84, 2) * PI)
        draw_line(end_point, v_two, l, d + 1, md,r )

def circle_nine(x, y, r):
    translate(x, y)

    noFill()
    strokeWeight(4)


    for i in range(8):
        rotate(radians(i * 45))
        colorIndex =  int(random(len(plates[selected_plates])))
        useColor= plates[selected_plates][colorIndex]
        stroke(useColor)

        draw_line((0, 0), PVector(2, 2), 12, 1, 10, r)


def circle_ten(x, y, r):

    #translate(x, y)
    noFill()

    strokeCap(ROUND)
    strokeWeight(4)

    count = 60
    for j in range(count):
        points = []
        for i in range(0, 360, 1):
            points.append(((r/2 - j*r/2/count)*sin(radians(i)), (r/2 - j*r/2/count)*cos(radians(i))))

        beginShape()
        for p in points:
            colorIndex =  int(random(len(plates[selected_plates])))
            useColor= plates[selected_plates][colorIndex]
            stroke(useColor)
            curveVertex(*p)
            if (random(1) < .1):
                endShape()
                beginShape()
        curveVertex(*points[0])
        curveVertex(*points[1])
        curveVertex(*points[2])
        endShape()


def circle_sixteen(x, y, r):
    translate(x, y)
    noFill()

    strokeCap(ROUND)
    strokeWeight(1)

    count = 700
    for j in range(count):
        points = []
        for i in range(0, 360, 1):
            points.append(((r/2 - j*r/2/count)*sin(radians(i)), (r/2 - j*r/2/count)*cos(radians(i))))

        beginShape()
        for p in points:
            if (random(1) < .6):
                colorIndex =  int(random(len(plates[selected_plates])))
                useColor= plates[selected_plates][colorIndex]
                stroke(useColor) 
                line(p[0], p[1], p[0] + random(-3, 3), p[1] + random(-3, 3))


def circle_seventeen(x, y, r):
    translate(x, y)
    noFill()

    strokeCap(ROUND)
    strokeWeight(1)

    count = 200
    for j in range(count):
        points = []
        for i in range(0, 360, 1):
            points.append(((r/2 - j*r/2/count)*sin(radians(i)), (r/2 - j*r/2/count)*cos(radians(i))))
            colorIndex =  int(random(len(plates[selected_plates])))
            useColor= plates[selected_plates][colorIndex]
            stroke(useColor)
        beginShape()
        for p in points:
            if (random(1) < .6):
                line(p[0], p[1], p[0] + random(-3, 3), p[1] + random(-3, 3))

##################
#
# Helper functions
#
##################

def draw_random_points_between(p1, p2, n, d):
    for i in range(n):
        u = random(1)

        x_dev = random(-d, d)
        y_dev = random(-d, d)

        point((1 - u)*p1[0] + u * p2[0] + x_dev, (1 - u)*p1[1] + u * p2[1] + y_dev)


# Used by: Many:
def distance(p1, p2):
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))

# Draw as many circle types as possible over time
def setup():
    size(w, h)
    background(0)
    pixelDensity(2)

    #circle_one(w/2, h/2, 900)
    #circle_four(w/2, h/2, 900, 4)
    #circle_five(w/2, h/2, 900, 10)
    #circle_six(w/2, h/2, 900, 2)
    #circle_seven(w/2, h/2, 900)
    circle_eight(w/2, h/2, 900)
    #circle_nine(w/2, h/2, 900)
    circle_ten(w/2, h/2, 900)
    #circle_sixteen(w/2, h/2, 900)
    #circle_seventeen(w/2, h/2, 900)

    save("Circles/circle-{}-{}{}.png".format(second(),month(), millis()))
