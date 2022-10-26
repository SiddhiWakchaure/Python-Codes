def type1():
    n1 = int(input("Enter number of faculty members for Maths:"))
    n2 = int(input("Enter number of faculty members for Graphics:"))
    n3 = int(input("Enter number of faculty members for Chem:"))
    n4 = int(input("Enter number of faculty members for Phy:"))
    n5 = int(input("Enter number of faculty members for PPS:"))
    n6 = int(input("Enter number of faculty members for BXE:"))
    n7 = int(input("Enter number of faculty members for BEE:"))
    n8 = int(input("Enter number of faculty members for EM:"))
    n9 = int(input("Enter number of faculty members for ES:"))
    EM2 = []
    G = []
    CHEM = []
    PHY = []
    PPS = []
    BXE = []
    BEE = []
    EM = []
    ES = []
    G1 = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8","G9","G10"]
    CM = ["C1", "C2", "C3","C4","C5","C6","C7","C8","C9","C10"]
    M = ["M1", "M2", "M3", "M4", "M5", "M6","M7","M8","M9","M10"]
    X = ["X1", "X2", "X3", "X4","X5", "X6", "X7", "X8","X9","X10"]
    PP = ["P1", "P2", "P3","P4","P5","P6","P7","P8","P9","P10"]
    PY = ["P1", "P2", "P3","P4", "P5", "P6","P7", "P8", "P9","P10"]
    E = ["E1", "E2", "E3", "E4","E5", "E6", "E7", "E8","E9","E10"]
    BE = ["B1", "B2", "B3","B4", "B5", "B6","B7", "B8", "B9","B10"]
    E1 = ["E1", "E2", "E3", "E4","E5", "E6", "E7", "E8","E9","E10"]
    for i in range(n1):
        EM2.append(M[i])
    for i in range(n2):
        G.append(G1[i])
    for i in range(n3):
        CHEM.append(CM[i])
    for i in range(n4):
        PHY.append(PY[i])
    for i in range(n5):
        PPS.append(PP[i])
    for i in range(n6):
        BXE.append(X[i])
    for i in range(n7):
        BEE.append(BE[i])
    for i in range(n8):
        EM.append(E[i])
    for i in range(n9):
        ES.append(E1[i])

    def tt1():
        l = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 1:-")
        print("  ")
        a = int(input("Enter faculty number for Graphics:"))
        b = int(input("Enter faculty number for ES:"))
        c = int(input("Enter faculty number for EM2:"))
        d = int(input("Enter faculty number for PPS:"))
        e = int(input("Enter faculty number for BXE:"))
        f = int(input("Enter faculty number for CHEM:"))
        for i in range(0, 20, 4):
            l[i] = G[a-1]
        for i in range(1, 20, 4):
            l[i] = ES[b-1]
        for i in range(2, 20, 4):
            l[i] = EM2[c-1]
        for i in range(3, 20, 4):
            l[i] = PPS[d-1]
        for i in range(4, 14, 4):
            l[i] = BXE[e-1]
        for i in range(5, 17, 4):
            l[i] = CHEM[f-1]
        l[1] = EM[f-1]
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 1                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "  |", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", "LAB", "    |", l[0], "     |", l[1], "       |", "LAB", "      |", l[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", "LAB", "    |", l[3], "     |", l[4], "       |", "LAB ", "     |", l[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", l[6], "     |", "LAB", "    |", l[7], "       |", l[8], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", l[9], "     |", "LAB", "    |", l[10], "       |", l[11], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", "LAB", "   |", l[12], "     |", "LAB", "       |", l[13], "      |", l[14], "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", "LAB", "   |", l[15], "     |", "LAB", "       |", l[16], "      |", l[17], "    |",)
        print("________________________________________________________________________")

        x = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 2:-")
        print("  ")
        a1 = int(input("Enter faculty number for ES:"))
        b1 = int(input("Enter faculty number for Graphics:"))
        c1 = int(input("Enter faculty number for EM2:"))
        d1 = int(input("Enter faculty number for PPS:"))
        e1 = int(input("Enter faculty number for BXE:"))
        f1 = int(input("Enter faculty number for CHEM:"))
        for i in range(0, 20, 4):
            x[i] = ES[a1-1]
        for i in range(1, 20, 4):
            x[i] = G[b1-1]
        for i in range(2, 14, 4):
            x[i] = EM2[c1-1]
        for i in range(3, 20, 4):
            x[i] = PPS[d1-1]
        for i in range(4, 20, 4):
            x[i] = BXE[e1-1]
        for i in range(5, 20, 4):
            x[i] = CHEM[f1-1]
        # x[14]=G[0]
        if l[1] == x[1]:
            x[1] = " "
        elif l[4] == x[4]:
            x[4] = " "
        elif l[8] == x[7]:
            x[7] = " "
        elif l[11] == x[10]:
            x[10] = " "
        elif l[14] == x[14]:
            x[14] = " "
        elif l[17] == x[17]:
            x[17] = " "
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 2                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("_____________________________________________________________________")
        print("8 to 9am ", "|", x[0], "   |", "LAB", "     |", x[1], "       |", x[2], "      |", "LAB", "    |",)
        print("_____________________________________________________________________")
        print("9 - 10am ", "|", x[3], "   |", "LAB", "     |", x[4], "       |", x[5], "      |", "LAB", "    |",)
        print("_____________________________________________________________________")
        print("                  BREAK      ")
        print("_____________________________________________________________________")
        print("10:15am  ", "|", "LAB", "  |", x[6], "     |", "LAB", "       |", x[7], "      |", x[8], "    |",)
        print("_____________________________________________________________________")
        print("11:15am  ", "|", "LAB", "  |", x[9], "     |", "LAB", "       |", x[10], "      |", x[11], "    |",)
        print("_____________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("_____________________________________________________________________")
        print("1 to 2pm ", "|", x[12], "  |", "LAB", "     |", x[13], "        |", "LAB", "      |", x[14], "    |",)
        print("_____________________________________________________________________")
        print("2 to 3pm ", "|", x[15], "  |", "LAB", "     |", x[16], "        |", "LAB", "      |", x[17], "    |",)
        print("_____________________________________________________________________")

        y = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 3:-")
        print("  ")
        a2 = int(input("Enter faculty number for Graphics:"))
        b2 = int(input("Enter faculty number for ES:"))
        c2 = int(input("Enter faculty number for EM2:"))
        d2 = int(input("Enter faculty number for CHEM:"))
        e2 = int(input("Enter faculty number for BXE:"))
        f2 = int(input("Enter faculty number for PPS:"))
        for i in range(0, 20, 4):
            y[i] = G[a2-1]
        for i in range(1, 20, 4):
            y[i] = ES[b2-1]
        for i in range(2, 20, 4):
            y[i] = EM2[c2-1]
        for i in range(3, 20, 4):
            y[i] = CHEM[d2-1]
        for i in range(4, 16, 4):
            y[i] = BXE[e2-1]
        for i in range(5, 20, 4):
            y[i] = PPS[f2-1]
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 3                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", "LAB", "  |", y[0], "     |", "LAB", "       |", y[1], "      |", y[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", "LAB", "  |", y[3], "     |", "LAB", "       |", y[4], "      |", y[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", y[6], "   |", "LAB", "    |", y[7], "       |", "LAB", "     |", y[8], "     |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", y[9], "   |", "LAB", "    |", y[10], "       |", "LAB", "     |", y[11], "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", y[12], "   |", y[13], "     |", "LAB", "       |", y[14], "     |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", y[15], "   |", y[16], "     |", "LAB", "       |", y[17], "     |", "LAB", "    |",)
        print("________________________________________________________________________")

        z = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 4:-")
        print("  ")
        a3 = int(input("Enter faculty number for ES:"))
        b3 = int(input("Enter faculty number for Graphics:"))
        c3 = int(input("Enter faculty number for BXE:"))
        d3 = int(input("Enter faculty number for PPS:"))
        e3 = int(input("Enter faculty number for EM2:"))
        f3 = int(input("Enter faculty number for CHEM:"))
        for i in range(0, 20, 4):
            z[i] = ES[a3-1]
        for i in range(1, 20, 4):
            z[i] = G[b3-1]
        for i in range(2, 14, 4):
            z[i] = BXE[c3-1]
        for i in range(3, 20, 4):
            z[i] = PPS[d3-1]
        for i in range(4, 20, 4):
            z[i] = EM2[e3-1]
        for i in range(5, 20, 4):
            z[i] = CHEM[f3-1]
        z[14] = G[b3-1]
        if y[6] == z[6]:
            z[6] = " "
        elif y[9] == z[9]:
            z[9] = " "
        elif y[13] == z[12]:
            z[12] = " "
        elif y[16] == z[15]:
            z[15] = " "
        elif y[2] == z[2]:
            z[2] = " "
        elif y[5] == z[5]:
            z[5] = " "
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 4                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", z[0], "    |", "LAB", "     |", z[1], "      |", "LAB", "      |", z[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", z[3], "    |", "LAB", "      |", z[4], "     |", "LAB", "      |", z[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", z[6], "    |", z[7], "      |", "LAB", "     |", z[8], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", z[9], "    |", z[10], "      |", "LAB", "     |", z[11], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", "LAB", "   |", z[12], "     |", z[13], "       |", "LAB", "      |", z[14], "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", "LAB", "   |", z[15], "       |", z[16], "     |", "LAB", "      |", z[17], "    |",)
        print("________________________________________________________________________")

        l1 = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 5:-")
        print("  ")
        a4 = int(input("Enter faculty number for Graphics:"))
        b4 = int(input("Enter faculty number for ES:"))
        c4 = int(input("Enter faculty number for EM2:"))
        d4 = int(input("Enter faculty number for PPS:"))
        e4 = int(input("Enter faculty number for BXE:"))
        f4 = int(input("Enter faculty number for CHEM:"))
        for i in range(0, 20, 4):
            l1[i] = G[a4-1]
        for i in range(1, 20, 4):
            l1[i] = ES[b4-1]
        for i in range(2, 20, 4):
            l1[i] = EM2[c4-1]
        for i in range(3, 20, 4):
            l1[i] = PPS[d4-1]
        for i in range(4, 16, 4):
            l1[i] = BXE[e4-1]
        for i in range(5, 20, 4):
            l1[i] = CHEM[f4-1]
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 5                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", l1[0], "    |", l1[1], "     |", "LAB", "       |", l1[2], "      |", "LAB", "   |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", l1[3], "    |", l1[4], "     |", "LAB", "       |", l1[5], "      |", "LAB", "   |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", "LAB", "  |", l1[6], "     |", l1[7], "       |", "LAB", "     |", l1[8], "     |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", "LAB", "  |", l1[9], "     |", l1[10], "       |", "LAB", "     |", l1[11], "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", l1[12], "  |", "LAB", "     |", l1[13], "       |", l1[14], "     |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", l1[15], " |", "LAB", "     |", l1[16], "       |", l1[17], "     |", "LAB", "    |",)
        print("________________________________________________________________________")

        x1 = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 11:-")
        print("  ")
        a5 = int(input("Enter faculty number for ES:"))
        b5 = int(input("Enter faculty number for Graphics:"))
        c5 = int(input("Enter faculty number for BXE:"))
        d5 = int(input("Enter faculty number for PPS:"))
        e5 = int(input("Enter faculty number for EM2:"))
        f5 = int(input("Enter faculty number for CHEM:"))
        for i in range(0, 20, 3):
            x1[i] = ES[a5-1]
        for i in range(1, 20, 3):
            x1[i] = G[b5-1]
        for i in range(2, 20, 3):
            x1[i] = BXE[c5-1]
        for i in range(3, 15, 3):
            x1[i] = PPS[d5-1]
        for i in range(4, 16, 3):
            x1[i] = EM2[e5-1]
        for i in range(5, 17, 3):
            x1[i] = CHEM[f5-1]
        if l1[12] == x1[5]:
            x1[5] = " "
        elif l1[15] == x1[10]:
            x1[10] = " "
        elif l1[13] == x1[7]:
            x1[7] = " "
        elif l1[16] == x1[12]:
            x1[12] = " "
        elif l1[14] == x1[8]:
            x1[8] = " "
        print("  ")
        print("  ")
        print("   FE11  ")
        print("    ")
        print("  TIME   ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("__________________________________________________________")
        print(" 12 - 1  ", "|", x1[0], "    |", x1[1], "     |", x1[2], "       |", x1[3], "      |", x1[4], "    |",)
        print("__________________________________________________________")
        print(" 1 - 2   ", "|", x1[5], "    |", x1[6], "     |", x1[7], "       |", x1[8], "      |", x1[9], "    |",)
        print("__________________________________________________________")
        print("               LUNCH BREAK      ")
        print("__________________________________________________________")
        print("2:45-3:45", "|", x1[10], "    |", x1[11], "    |", x1[12], "       |", "LAB", "      |", x1[13], "    |",)
        print("__________________________________________________________")
        print("3:45-4:45", "|", x1[14], "    |", x1[15], "    |", x1[16], "       |", "LAB", "      |", x1[17], "    |",)
        print("__________________________________________________________")
        print("                  BREAK      ")
        print("__________________________________________________________")
        print(" 5 - 7   ", "|", "LAB", "  |", "LAB", "     |", "LAB", "       |", "LAB", "      |", "LAB", " |",)

        l2 = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 6:-")
        print("  ")
        a6 = int(input("Enter faculty number for ES:"))
        b6 = int(input("Enter faculty number for EM:"))
        c6 = int(input("Enter faculty number for EM2:"))
        d6 = int(input("Enter faculty number for Graphics:"))
        e6 = int(input("Enter faculty number for BEE:"))
        f6 = int(input("Enter faculty number for PHY:"))
        for i in range(0, 20, 5):
            l2[i] = ES[a6-1]
        for i in range(1, 20, 5):
            l2[i] = EM[b6-1]
        for i in range(2, 20, 5):
            l2[i] = EM2[c6-1]
        for i in range(3, 20, 5):
            l2[i] = G[d6-1]
        for i in range(4, 20, 5):
            l2[i] = BEE[e6-1]
        for i in range(5, 20, 5):
            l2[i] = PHY[f6-1]
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 6                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", "LAB", "  |", l2[0], "     |", "LAB", "       |", l2[1], "      |", l2[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", "LAB", "  |", l2[3], "     |", "LAB", "       |", l2[4], "      |", l2[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", l2[6], "  |", "LAB", "    |", l2[7], "       |", "LAB", "     |", l2[8], "     |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", l2[9], "  |", "LAB", "    |", l2[10], "       |", "LAB", "     |", l2[11], "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", l2[12], "  |", l2[13], "     |", "LAB", "       |", l2[14], "     |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", l2[15], " |", l2[16], "     |", "LAB", "       |", l2[17], "     |", "LAB", "    |",)
        print("________________________________________________________________________")

        x2 = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 7:-")
        print("  ")
        a7 = int(input("Enter faculty number for Graphics:"))
        b7 = int(input("Enter faculty number for ES:"))
        c7 = int(input("Enter faculty number for EM2:"))
        d7 = int(input("Enter faculty number for BEE:"))
        e7 = int(input("Enter faculty number for PHY:"))
        f7 = int(input("Enter faculty number for EM:"))
        for i in range(0, 20, 4):
            x2[i] = G[a7-1]
        for i in range(1, 20, 4):
            x2[i] = ES[b7-1]
        for i in range(2, 20, 4):
            x2[i] = EM2[c7-1]
        for i in range(3, 15, 4):
            x2[i] = BEE[d7-1]
        for i in range(4, 20, 4):
            x2[i] = PHY[e7-1]
        for i in range(5, 20, 4):
            x2[i] = EM[f7-1]
        x2[15] = G[a7-1]
        if l2[6] == x2[6]:
            x2[6] = " "
        elif l2[9] == x2[9]:
            x2[9] = ""
        elif l2[13] == x2[12]:
            x2[12] = " "
        elif l2[16] == x2[15]:
            x2[15] = " "
        elif l2[2] == x2[2]:
            x2[2] = " "
        elif l2[5] == x2[5]:
            x2[5] = " "
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 7                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", x2[0], "  |", "LAB", "     |", x2[1], "       |", "LAB", "      |", x2[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", x2[3], "  |", "LAB", "     |", x2[4], "       |", "LAB", "      |", x2[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", x2[6], "  |", x2[7], "    |", "LAB", "     |", x2[8], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", x2[9], "  |", x2[10], "    |", "LAB", "      |", x2[11], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", "LAB", "  |", x2[12], "     |", x2[13], "       |", "LAB", "      |", x2[14], "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", "LAB", "  |", x2[15], "     |", x2[16], "      |", "LAB", "      |", x2[17], "    |",)
        print("________________________________________________________________________")

        l3 = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 8:-")
        print("  ")
        a8 = int(input("Enter faculty number for ES:"))
        b8 = int(input("Enter faculty number for EM:"))
        c8 = int(input("Enter faculty number for EM2:"))
        d8 = int(input("Enter faculty number for Graphics:"))
        e8 = int(input("Enter faculty number for BEE:"))
        f8 = int(input("Enter faculty number for PHY:"))
        for i in range(0, 20, 5):
            l3[i] = ES[a8-1]
        for i in range(1, 20, 5):
            l3[i] = EM[b8-1]
        for i in range(2, 20, 5):
            l3[i] = EM2[c8-1]
        for i in range(3, 13, 5):
            l3[i] = G[d8-1]
        for i in range(4, 20, 5):
            l3[i] = BEE[e8-1]
        for i in range(5, 20, 5):
            l3[i] = PHY[f8-1]
        l3[13] = PHY[f8-1]
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 8                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", l3[0], "  |", l3[1], "     |", l3[2], "       |", l3[3], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", l3[4], "  |", l3[5], "     |", l3[6], "       |", l3[7], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", "LAB", "  |", l3[8], "    |", "LAB", "       |", "LAB", "     |", l3[9], "     |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", "LAB", "  |", l3[10], "    |", "LAB", "       |", "LAB", "     |", l3[11], "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", l3[12], "  |", "LAB", "     |", l3[13], "       |", l3[14], "     |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", l3[15], " |", "LAB", "     |", l3[16], "       |", l3[17], "     |", "LAB", "    |",)
        print("________________________________________________________________________")

        x3 = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 9:-")
        print("  ")
        a9 = int(input("Enter faculty number for ES:"))
        b9 = int(input("Enter faculty number for Graphics:"))
        c9 = int(input("Enter faculty number for EM2:"))
        d9 = int(input("Enter faculty number for BEE:"))
        e9 = int(input("Enter faculty number for EM:"))
        f9 = int(input("Enter faculty number for PHY:"))
        for i in range(0, 20, 4):
            x3[i] = ES[a9-1]
        for i in range(1, 20, 4):
            x3[i] = G[b9-1]
        for i in range(2, 20, 4):
            x3[i] = EM2[c9-1]
        for i in range(3, 15, 4):
            x3[i] = BEE[d9-1]
        for i in range(4, 20, 4):
            x3[i] = EM[e9-1]
        for i in range(5, 20, 4):
            x3[i] = PHY[f9-1]
        x3[15] = G[b9-1]
        if l3[1] == x3[0]:
            x3[0] = " "
        elif l3[5] == x3[3]:
            x3[3] = " "
        elif l3[13] == x3[12]:
            x3[12] = " "
        elif l3[2] == x3[1]:
            x3[1] = " "
        elif l3[6] == x3[4]:
            x3[4] = " "
        elif l3[14] == x3[13]:
            x3[13] = " "
        elif l3[17] == x3[16]:
            x3[16] = " "
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 9                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", "LAB", "  |", x3[0], "     |", x3[1], "       |", "LAB", "      |", x3[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", "LAB", "  |", x3[3], "     |", x3[4], "       |", "LAB ", "     |", x3[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", x3[6], "  |", "LAB", "    |", x3[7], "       |", x3[8], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", x3[9], "  |", "LAB", "    |", x3[10], "       |", x3[11], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", "LAB", "  |", x3[12], "     |", "LAB", "       |", x3[13], "      |", x3[14], "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", "LAB", "  |", x3[15], "     |", "LAB", "       |", x3[16], "      |", x3[17], "    |",)
        print("________________________________________________________________________")

        l4 = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", ]
        print(" ")
        print("For FE 10:-")
        print("  ")
        a10 = int(input("Enter faculty number for ES:"))
        b10 = int(input("Enter faculty number for EM:"))
        c10 = int(input("Enter faculty number for Graphics:"))
        d10 = int(input("Enter faculty number for EM2:"))
        e10 = int(input("Enter faculty number for BEE:"))
        f10 = int(input("Enter faculty number for PHY:"))
        for i in range(0, 20, 3):
            l4[i] = ES[a10-1]
        for i in range(1, 20, 3):
            l4[i] = EM[b10-1]
        for i in range(2, 20, 3):
            l4[i] = G[c10-1]
        for i in range(3, 20, 3):
            l4[i] = EM2[d10-1]
        for i in range(4, 13, 3):
            l4[i] = BEE[e10-1]
        for i in range(5, 17, 3):
            l4[i] = PHY[f10-1]
        l4[15] = EM[b10-1]
        print("")
        print(" FE10  ")
        print("  TIME   ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("__________________________________________________________")
        print(" 12 - 1  ", "|", l4[0], "    |", l4[1], "     |", l4[2], "       |", l4[3], "      |", l4[4], "    |",)
        print("__________________________________________________________")
        print(" 1 - 2   ", "|", l4[5], "    |", l4[6], "     |", l4[7], "       |", l4[8], "      |", l4[9], "    |",)
        print("__________________________________________________________")
        print("               LUNCH BREAK      ")
        print("__________________________________________________________")
        print("2:45-3:45", "|", l4[10], "    |", "LAB", "    |", l4[11], "       |", l4[12], "      |", l4[13], "    |",)
        print("__________________________________________________________")
        print("3:45-4:45", "|", l4[14], "    |", "LAB", "    |", l4[15], "       |", l4[16], "      |", l4[17], "    |",)
        print("__________________________________________________________")
        print("                  BREAK      ")
        print("__________________________________________________________")
        print(" 5 - 7   ", "|", "LAB", "  |", "LAB", "     |", "LAB", "       |", "LAB", "      |", "LAB", " |",)
    tt1()


def type2():
    n1 = int(input("Enter number of faculty members for Maths:"))
    n2 = int(input("Enter number of faculty members for SME:"))
    n3 = int(input("Enter number of faculty members for Chem:"))
    n4 = int(input("Enter number of faculty members for Phy:"))
    n5 = int(input("Enter number of faculty members for PPS:"))
    n6 = int(input("Enter number of faculty members for BXE:"))
    n7 = int(input("Enter number of faculty members for BEE:"))
    n8 = int(input("Enter number of faculty members for EM:"))
    n9 = int(input("Enter number of faculty members for ES:"))
    EM1=[]
    SME=[]
    CHEM=[]
    PHY=[]
    PPS=[]
    BXE=[]
    BEE=[]
    EM=[]
    ES=[]
    G = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8","G9","G10"]
    CM = ["C1", "C2", "C3","C4","C5","C6", "C7", "C8","C9","C10"]
    E2 = ["M1", "M2", "M3", "M4", "M5", "M6","M7","M8","M9","M10"]
    X = ["X1", "X2", "X3", "X4","X5","X6","X7","X8","X9","X10"]
    PP = ["P1", "P2", "P3","P4","P5","P6","P7","P8","P9","P10"]
    PH = ["P1", "P2", "P3","P4","P5","P6","P7","P8","P9","P10"]
    E = ["E1", "E2", "E3", "E4","E5","E6","E7", "E8", "E9","E10"]
    B = ["B1", "B2", "B3","B4","B5","B6","B7", "B8","B9","B10"]
    E1 = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10"]
    for i in range(n1):
        EM1.append(E2[i])
    for i in range(n2):
        SME.append(G[i])
    for i in range(n3):
        CHEM.append(CM[i])
    for i in range(n4):
        PHY.append(PH[i])
    for i in range(n5):
        PPS.append(PP[i])
    for i in range(n6):
        BXE.append(X[i])
    for i in range(n7):
        BEE.append(B[i])
    for i in range(n8):
        EM.append(E[i])
    for i in range(n9):
        ES.append(E1[i])
    def tt1():
        l = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print("  ")
        print("For FE1:")
        print("  ")
        a = int(input("Enter faculty number for SME:"))
        b = int(input("Enter faculty number for ES:"))
        c = int(input("Enter faculty number for EM1:"))
        d = int(input("Enter faculty number for PHY:"))
        e = int(input("Enter faculty number for BEE:"))
        f = int(input("Enter faculty number for EM:"))
        for i in range(0, 20, 4):
            l[i] = G[a-1]
        for i in range(1, 20, 4):
            l[i] = ES[b-1]
        for i in range(2, 20, 4):
            l[i] = EM1[c-1]
        for i in range(3, 20, 4):
            l[i] = PHY[d-1]
        for i in range(4, 14, 4):
            l[i] = BEE[e-1]
        for i in range(5, 17, 4):
            l[i] = EM[f-1]
        l[1] = EM[f-1]
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 1                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "  |", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", "LAB", "    |", l[0], "     |", l[1], "       |", "LAB", "      |", l[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", "LAB", "    |", l[3], "     |", l[4], "       |", "LAB ", "     |", l[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", l[6], "     |", "LAB", "    |", l[7], "       |", l[8], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", l[9], "     |", "LAB", "    |", l[10], "       |", l[11], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", "LAB", "   |", l[12], "     |", "LAB", "       |", l[13], "      |", l[14], "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", "LAB", "   |", l[15], "     |", "LAB", "       |", l[16], "      |", l[17], "    |",)
        print("________________________________________________________________________")

        x = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print("  ")
        print("For FE2:")
        print("  ")
        a1 = int(input("Enter faculty number for ES:"))
        b1 = int(input("Enter faculty number for SME:"))
        c1 = int(input("Enter faculty number for BEE:"))
        d1 = int(input("Enter faculty number for PHY:"))
        e1 = int(input("Enter faculty number for EM1:"))
        f1 = int(input("Enter faculty number for EM:"))
        for i in range(0, 20, 4):
            x[i] = ES[a1-1]
        for i in range(1, 20, 4):
            x[i] = G[b1-1]
        for i in range(2, 14, 4):
            x[i] = BEE[c1-1]
        for i in range(3, 20, 4):
            x[i] = PHY[d1-1]
        for i in range(4, 20, 4):
            x[i] = EM1[e1-1]
        for i in range(5, 20, 4):
            x[i] = EM[f1-1]
        # x[14]=G[b1-1]
        if l[1] == x[1]:
            x[1] = " "
        elif l[4] == x[4]:
            x[4] = " "
        elif l[8] == x[7]:
            x[7] = " "
        elif l[11] == x[10]:
            x[10] = " "
        elif l[14] == x[14]:
            x[14] = " "
        elif l[17] == x[17]:
            x[17] = " "
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 2                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("_____________________________________________________________________")
        print("8 to 9am ", "|", x[0], "   |", "LAB", "     |", x[1], "       |", x[2], "      |", "LAB", "    |",)
        print("_____________________________________________________________________")
        print("9 - 10am ", "|", x[3], "   |", "LAB", "     |", x[4], "       |", x[5], "      |", "LAB", "    |",)
        print("_____________________________________________________________________")
        print("                  BREAK      ")
        print("_____________________________________________________________________")
        print("10:15am  ", "|", "LAB", "  |", x[6], "     |", "LAB", "       |", x[7], "      |", x[8], "    |",)
        print("_____________________________________________________________________")
        print("11:15am  ", "|", "LAB", "  |", x[9], "     |", "LAB", "       |", x[10], "      |", x[11], "    |",)
        print("_____________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("_____________________________________________________________________")
        print("1 to 2pm ", "|", x[12], "  |", "LAB", "     |", x[13], "        |", "LAB", "      |", x[14], "    |",)
        print("_____________________________________________________________________")
        print("2 to 3pm ", "|", x[15], "  |", "LAB", "     |", x[16], "        |", "LAB", "      |", x[17], "    |",)
        print("_____________________________________________________________________")
    tt1()
    def tt2():
        l = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 3:-")
        print(" ")
        a = int(input("Enter faculty number for SME:"))
        b = int(input("Enter faculty number for ES:"))
        c = int(input("Enter faculty number for EM1:"))
        d = int(input("Enter faculty number for EM:"))
        e = int(input("Enter faculty number for BEE:"))
        f = int(input("Enter faculty number for PHY:"))
        for i in range(0, 20, 4):
            l[i] = G[a-1]
        for i in range(1, 20, 4):
            l[i] = ES[b-1]
        for i in range(2, 20, 4):
            l[i] = EM1[c-1]
        for i in range(3, 20, 4):
            l[i] = EM[d-1]
        for i in range(4, 16, 4):
            l[i] = BEE[e-1]
        for i in range(5, 20, 4):
            l[i] = PHY[f-1]
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 3                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", "LAB", "  |", l[0], "     |", "LAB", "       |", l[1], "      |", l[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", "LAB", "  |", l[3], "     |", "LAB", "       |", l[4], "      |", l[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", l[6], "   |", "LAB", "    |", l[7], "       |", "LAB", "     |", l[8], "     |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", l[9], "   |", "LAB", "    |", l[10], "       |", "LAB", "     |", l[11], "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", l[12], "   |", l[13], "     |", "LAB", "       |", l[14], "     |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", l[15], "   |", l[16], "     |", "LAB", "       |", l[17], "     |", "LAB", "    |",)
        print("________________________________________________________________________")

        x = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 4:-")
        print(" ")
        a1 = int(input("Enter faculty number for ES:"))
        b1 = int(input("Enter faculty number for SME:"))
        c1 = int(input("Enter faculty number for BEE:"))
        d1 = int(input("Enter faculty number for PHY:"))
        e1 = int(input("Enter faculty number for EM1:"))
        f1 = int(input("Enter faculty number for EM:"))
        for i in range(0, 20, 4):
            x[i] = ES[a1-1]
        for i in range(1, 20, 4):
            x[i] = G[b1-1]
        for i in range(2, 14, 4):
            x[i] = BEE[c1-1]
        for i in range(3, 20, 4):
            x[i] = PHY[d1-1]
        for i in range(4, 20, 4):
            x[i] = EM1[e1-1]
        for i in range(5, 20, 4):
            x[i] = EM[f1-1]
        x[14] = G[b1-1]
        if l[6] == x[6]:
            x[6] = " "
        elif l[9] == x[9]:
            x[9] = " "
        elif l[13] == x[12]:
            x[12] = " "
        elif l[16] == x[15]:
            x[15] = " "
        elif l[2] == x[2]:
            x[2] = " "
        elif l[5] == x[5]:
            x[5] = " "
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 4                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", x[0], "    |", "LAB", "     |", x[1], "      |", "LAB", "      |", x[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", x[3], "    |", "LAB", "      |", x[4], "     |", "LAB", "      |", x[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", x[6], "    |", x[7], "      |", "LAB", "     |", x[8], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", x[9], "    |", x[10], "      |", "LAB", "     |", x[11], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", "LAB", "   |", x[12], "     |", x[13], "       |", "LAB", "      |", x[14], "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", "LAB", "   |", x[15], "       |", x[16], "     |", "LAB", "      |", x[17], "    |",)
        print("________________________________________________________________________")
    tt2()
    def tt3():
        l = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 5:-")
        print(" ")
        a = int(input("Enter faculty number for SME:"))
        b = int(input("Enter faculty number for ES:"))
        c = int(input("Enter faculty number for EM1:"))
        d = int(input("Enter faculty number for PHY:"))
        e = int(input("Enter faculty number for BEE:"))
        f = int(input("Enter faculty number for EM:"))
        for i in range(0, 20, 4):
            l[i] = G[a-1]
        for i in range(1, 20, 4):
            l[i] = ES[b-1]
        for i in range(2, 20, 4):
            l[i] = EM1[c-1]
        for i in range(3, 20, 4):
            l[i] = PHY[d-1]
        for i in range(4, 16, 4):
            l[i] = BEE[e-1]
        for i in range(5, 20, 4):
            l[i] = EM[f-1]
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 5                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", l[0], "    |", l[1], "     |", "LAB", "       |", l[2], "      |", "LAB", "   |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", l[3], "    |", l[4], "     |", "LAB", "       |", l[5], "      |", "LAB", "   |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", "LAB", "  |", l[6], "     |", l[7], "       |", "LAB", "     |", l[8], "     |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", "LAB", "  |", l[9], "     |", l[10], "       |", "LAB", "     |", l[11], "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", l[12], "  |", "LAB", "     |", l[13], "       |", l[14], "     |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", l[15], " |", "LAB", "     |", l[16], "       |", l[17], "     |", "LAB", "    |",)
        print("________________________________________________________________________")

        x = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE11:-")
        print(" ")
        a1 = int(input("Enter faculty number for ES:"))
        b1 = int(input("Enter faculty number for SME:"))
        c1 = int(input("Enter faculty number for BEE:"))
        d1 = int(input("Enter faculty number for PHY:"))
        e1 = int(input("Enter faculty number for EM1:"))
        f1 = int(input("Enter faculty number for EM:"))
        for i in range(0, 20, 3):
            x[i] = ES[a1-1]
        for i in range(1, 20, 3):
            x[i] = G[b1-1]
        for i in range(2, 20, 3):
            x[i] = BEE[c1-1]
        for i in range(3, 15, 3):
            x[i] = PHY[d1-1]
        for i in range(4, 16, 3):
            x[i] = EM1[e1-1]
        for i in range(5, 17, 3):
            x[i] = EM[f1-1]
        if l[12] == x[5]:
            x[5] = " "
        elif l[15] == x[10]:
            x[10] = " "
        elif l[13] == x[7]:
            x[7] = " "
        elif l[16] == x[12]:
            x[12] = " "
        elif l[14] == x[8]:
            x[8] = " "
        print("  ")
        print("  ")
        print("   FE11  ")
        print("    ")
        print("  TIME   ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("__________________________________________________________")
        print(" 12 - 1  ", "|", x[0], "    |", x[1], "     |", x[2], "       |", x[3], "      |", x[4], "    |",)
        print("__________________________________________________________")
        print(" 1 - 2   ", "|", x[5], "    |", x[6], "     |", x[7], "       |", x[8], "      |", x[9], "    |",)
        print("__________________________________________________________")
        print("               LUNCH BREAK      ")
        print("__________________________________________________________")
        print("2:45-3:45", "|", x[10], "    |", x[11], "    |", x[12], "       |", "LAB", "      |", x[13], "    |",)
        print("__________________________________________________________")
        print("3:45-4:45", "|", x[14], "    |", x[15], "    |", x[16], "       |", "LAB", "      |", x[17], "    |",)
        print("__________________________________________________________")
        print("                  BREAK      ")
        print("__________________________________________________________")
        print(" 5 - 7   ", "|", "LAB", "  |", "LAB", "     |", "LAB", "       |", "LAB", "      |", "LAB", " |",)
    tt3()
    def tt4():
        l = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 6:-")
        print(" ")
        a = int(input("Enter faculty number for ES:"))
        b = int(input("Enter faculty number for CHEM:"))
        c = int(input("Enter faculty number for EM1:"))
        d = int(input("Enter faculty number for SME:"))
        e = int(input("Enter faculty number for BXE:"))
        f = int(input("Enter faculty number for PPS:"))
        for i in range(0, 20, 5):
            l[i] = ES[a-1]
        for i in range(1, 20, 5):
            l[i] = CHEM[b-1]
        for i in range(2, 20, 5):
            l[i] = EM1[c-1]
        for i in range(3, 20, 5):
            l[i] = G[d-1]
        for i in range(4, 20, 5):
            l[i] = BXE[e-1]
        for i in range(5, 20, 5):
            l[i] = PPS[f-1]
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 6                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", "LAB", "  |", l[0], "     |", "LAB", "       |", l[1], "      |", l[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", "LAB", "  |", l[3], "     |", "LAB", "       |", l[4], "      |", l[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", l[6], "  |", "LAB", "    |", l[7], "       |", "LAB", "     |", l[8], "     |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", l[9], "  |", "LAB", "    |", l[10], "       |", "LAB", "     |", l[11], "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", l[12], "  |", l[13], "     |", "LAB", "       |", l[14], "     |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", l[15], " |", l[16], "     |", "LAB", "       |", l[17], "     |", "LAB", "    |",)
        print("________________________________________________________________________")

        x = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 7:-")
        print(" ")
        a1 = int(input("Enter faculty number for SME:"))
        b1 = int(input("Enter faculty number for ES:"))
        c1 = int(input("Enter faculty number for EM1:"))
        d1 = int(input("Enter faculty number for BXE:"))
        e1 = int(input("Enter faculty number for PPS:"))
        f1 = int(input("Enter faculty number for CHEM:"))
        for i in range(0, 20, 4):
            x[i] = G[a1-1]
        for i in range(1, 20, 4):
            x[i] = ES[b1-1]
        for i in range(2, 20, 4):
            x[i] = EM1[c1-1]
        for i in range(3, 15, 4):
            x[i] = BXE[d1-1]
        for i in range(4, 20, 4):
            x[i] = PPS[e1-1]
        for i in range(5, 20, 4):
            x[i] = CHEM[f1-1]
        if l[6] == x[6]:
            x[6] = " "
        elif l[9] == x[9]:
            x[9] = ""
        elif l[13] == x[12]:
            x[12] = " "
        elif l[16] == x[15]:
            x[15] = " "
        elif l[2] == x[2]:
            x[2] = " "
        elif l[5] == x[5]:
            x[5] = " "
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 7                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", x[0], "  |", "LAB", "     |", x[1], "       |", "LAB", "      |", x[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", x[3], "  |", "LAB", "     |", x[4], "       |", "LAB", "      |", x[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", x[6], "  |", x[7], "    |", "LAB", "     |", x[8], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", x[9], "  |", x[10], "    |", "LAB", "      |", x[11], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", "LAB", "  |", x[12], "     |", x[13], "       |", "LAB", "      |", x[14], "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", "LAB", "  |", x[15], "     |", x[16], "      |", "LAB", "      |", x[17], "    |",)
        print("________________________________________________________________________")

        y = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 8:-")
        print(" ")
        a2 = int(input("Enter faculty number for ES:"))
        b2 = int(input("Enter faculty number for CHEM:"))
        c2 = int(input("Enter faculty number for EM1:"))
        d2 = int(input("Enter faculty number for SME:"))
        e2 = int(input("Enter faculty number for BXE:"))
        f2 = int(input("Enter faculty number for PPS:"))
        for i in range(0, 20, 5):
            y[i] = ES[a2-1]
        for i in range(1, 20, 5):
            y[i] = CHEM[b2-1]
        for i in range(2, 20, 5):
            y[i] = EM1[c2-1]
        for i in range(3, 13, 5):
            y[i] = G[d2-1]
        for i in range(4, 20, 5):
            y[i] = BXE[e2-1]
        for i in range(5, 20, 5):
            y[i] = PPS[f2-1]
        if x[0]==y[0]:
            y[0]=" "
        elif x[3]==y[4]:
            y[4]=" "
        elif x[7]==y[8]:
            y[8]=" "
        elif x[10]==y[10]:
            y[10]=" "
        elif x[1]==y[2]:
            y[2]=" "
        elif x[4]==y[6]:
            y[6]=" "
        elif x[13]==y[16]:
            y[16]=" "
        elif l[12]==y[12]:
            y[16]=" "
        elif l[15]==y[15]:
            y[16]=" "
        elif l[0]==y[1]:
            y[1]=" "
        elif l[3]==y[5]:
            y[5]=" "
        elif l[1]==y[3]:
            y[3]=" "
        elif l[4]==y[7]:
            y[7]=" "
        elif l[14]==y[14]:
            y[14]=" "
        elif l[17]==y[17]:
            y[17]=" "
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 8                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", y[0], "  |", y[1], "     |", y[2], "       |", y[3], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", y[4], "  |", y[5], "     |", y[6], "       |", y[7], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", "LAB", "  |", y[8], "    |", "LAB", "       |", "LAB", "     |", y[9], "     |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", "LAB", "  |", y[10], "    |", "LAB", "       |", "LAB", "     |", y[11], "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", y[12], "  |", "LAB", "     |", y[13], "       |", y[14], "     |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", y[15], " |", "LAB", "     |", y[16], "       |", y[17], "     |", "LAB", "    |",)
        print("________________________________________________________________________")
    tt4()
    def tt5():
        x = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        print(" ")
        print("For FE 9:-")
        print(" ")
        a = int(input("Enter faculty number for ES:"))
        b = int(input("Enter faculty number for SME:"))
        c = int(input("Enter faculty number for EM1:"))
        d = int(input("Enter faculty number for BXE:"))
        e = int(input("Enter faculty number for CHEM:"))
        f = int(input("Enter faculty number for PPS:"))
        for i in range(0, 20, 4):
            x[i] = ES[a-1]
        for i in range(1, 20, 4):
            x[i] = G[b-1]
        for i in range(2, 20, 4):
            x[i] = EM1[c-1]
        for i in range(3, 15, 4):
            x[i] = BXE[d-1]
        for i in range(4, 20, 4):
            x[i] = CHEM[e-1]
        for i in range(5, 20, 4):
            x[i] = PPS[f-1]
        print("                                                                                                    ")
        print("                                                                                                    ")
        print("  FE 9                                                                                              ")
        print("                                                                                                    ")
        print("         ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("________________________________________________________________________")
        print("8 to 9am ", "|", "LAB", "  |", x[0], "     |", x[1], "       |", "LAB", "      |", x[2], "    |",)
        print("________________________________________________________________________")
        print("9 - 10am ", "|", "LAB", "  |", x[3], "     |", x[4], "       |", "LAB ", "     |", x[5], "    |",)
        print("________________________________________________________________________")
        print("                  BREAK      ")
        print("________________________________________________________________________")
        print("10:15am  ", "|", x[6], "  |", "LAB", "    |", x[7], "       |", x[8], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("11:15am  ", "|", x[9], "  |", "LAB", "    |", x[10], "       |", x[11], "      |", "LAB", "    |",)
        print("________________________________________________________________________")
        print("                 LUNCH BREAK      ")
        print("________________________________________________________________________")
        print("1 to 2pm ", "|", "LAB", "  |", x[12], "     |", "LAB", "       |", x[13], "      |", x[14], "    |",)
        print("________________________________________________________________________")
        print("2 to 3pm ", "|", "LAB", "  |", x[15], "     |", "LAB", "       |", x[16], "      |", x[17], "    |",)
        print("________________________________________________________________________")

        l = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
             "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", ]
        print(" ")
        print("For FE10:-")
        print(" ")
        a1 = int(input("Enter faculty number for ES:"))
        b1 = int(input("Enter faculty number for CHEM:"))
        c1 = int(input("Enter faculty number for SME:"))
        d1 = int(input("Enter faculty number for EM1:"))
        e1 = int(input("Enter faculty number for BXE:"))
        f1 = int(input("Enter faculty number for PPS:"))
        for i in range(0, 20, 3):
            l[i] = ES[a1-1]
        for i in range(1, 20, 3):
            l[i] = CHEM[b1-1]
        for i in range(2, 20, 3):
            l[i] = G[c1-1]
        for i in range(3, 20, 3):
            l[i] = EM1[d1-1]
        for i in range(4, 13, 3):
            l[i] = BXE[e1-1]
        for i in range(5, 17, 3):
            l[i] = PPS[f1-1]
        if x[12] == l[6]:
            l[6]=" "
        elif x[13] == l[8]:
            l[8]=" "
        elif x[16] == l[12]:
            l[12]=" "
        elif x[14] == l[9]:
            l[9]=" "
        elif x[17] == l[13]:
            l[13]=" "
        print("")
        print(" FE10  ")
        print("  TIME   ", "|", "MONDAY", "|", "TUESDAY", "|", "WEDNESDAY", "|", "THURSDAY", "|", "FRIDAY", "|")
        print("__________________________________________________________")
        print(" 12 - 1  ", "|", l[0], "    |", l[1], "     |", l[2], "       |", l[3], "      |", l[4], "    |",)
        print("__________________________________________________________")
        print(" 1 - 2   ", "|", l[5], "    |", l[6], "     |", l[7], "       |", l[8], "      |", l[9], "    |",)
        print("__________________________________________________________")
        print("               LUNCH BREAK      ")
        print("__________________________________________________________")
        print("2:45-3:45", "|", l[10], "    |", "LAB", "    |", l[11], "       |", l[12], "      |", l[13], "    |",)
        print("__________________________________________________________")
        print("3:45-4:45", "|", l[14], "    |", "LAB", "    |", l[15], "       |", l[16], "      |", l[17], "    |",)
        print("__________________________________________________________")
        print("                  BREAK      ")
        print("__________________________________________________________")
        print(" 5 - 7   ", "|", "LAB", "  |", "LAB", "     |", "LAB", "       |", "LAB", "      |", "LAB", " |",)
    tt5()
m = int(input("View Timetables for sem 1 or 2?"))
if m == 1:
    type2()
elif m ==2:
    type1()