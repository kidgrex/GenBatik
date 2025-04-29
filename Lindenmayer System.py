import turtle

def l_system(axiom, rules, iterations):
    for _ in range(iterations):
        axiom = "".join(rules.get(c, c) for c in axiom)
    return axiom

def draw_l_system(axiom, angle, distance):
    turtle.register_shape("megamendung2.gif")
    turtle.shape("megamendung2.gif")
    turtle.penup()
    for command in axiom:
        if command == 'F':
            turtle.stamp()  # Cetak lingkaran di posisi saat ini
            turtle.forward(distance)  # Pindah ke posisi berikutnya
        elif command == '+':
            turtle.right(angle)
        elif command == '-':
            turtle.left(angle)

def main():
    axiom = "FX"
    rules = {
        "X": "X+YF+",
        "Y": "-FX-Y"
    }
    iterations = 7  # Sesuaikan jumlah iterasi untuk kompleksitas yang diinginkan
    angle = 90
    distance = 30  # Sesuaikan ukuran jarak antar lingkaran
    
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    
    instructions = l_system(axiom, rules, iterations)
    draw_l_system(instructions, angle, distance)
    
    turtle.done()

if __name__ == "__main__":
    main()