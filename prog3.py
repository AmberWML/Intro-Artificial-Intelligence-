from csp import*


a1 = backtracking_search(NQueensCSP(4))

a2 = backtracking_search(NQueensCSP(12))

a3 = backtracking_search(NQueensCSP(20))
print("Question 1 solution: (backtracking_search)")
print("Use the the AIMA backtracking-search function to solve the n-queens problem with 4 queens.")
print(a1)
print("Use the the AIMA backtracking-search function to solve the n-queens problem with 12 queens.")
print(a2)
print("Use the the AIMA backtracking-search function to solve the n-queens problem with 20 queens.")
print(a3)

print()
print("Question 2 solution:(forward_checking)")

b1 = backtracking_search(NQueensCSP(4),inference=forward_checking)

b2 = backtracking_search(NQueensCSP(12),inference=forward_checking)

b3 = backtracking_search(NQueensCSP(20),inference=forward_checking)

print("Use the the AIMA forward-checking function to solve the n-queens problem with 4 queens.")
print(b1)
print("Use the the AIMA forward-checking function to solve the n-queens problem with 12 queens.")
print(b2)
print("Use the the AIMA forward-checking function to solve the n-queens problem with 20 queens.")
print(b3)


print()
print("Question 3 solution: (Map coloring) ")
answer3 = MapColoringCSP(list('RGB'), """SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: """)
print(backtracking_search(answer3))

print()
print("Question 4 solution: (Map coloring of 4 colors)")
answer4 = MapColoringCSP(list('RGBP'), """SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: """)
print(backtracking_search(answer4))
print("Based on the result, 3 colors are enough, we do not need four colors.")

print()
print("Question 5 solution:( Map coloring of 2 colors) ")
answer5 = MapColoringCSP(list('RG'), """SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: """)
print(backtracking_search(answer5))
print("We fail to find the solution, this is not consistent.")

print()
print("Question 6 solution: (Map coloring by AC-3 algorithm) ")
answer6 = MapColoringCSP(list('RGB'), """SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: """)
print(AC3(answer6))

print()
print("Question 7 solution:(Map color for USA) ")
a7= MapColoringCSP(list('RGBP'),
                         """WA: OR ID; OR: ID NV CA; CA: NV AZ; NV: ID UT AZ; ID: MT WY UT;
                         UT: WY CO AZ; MT: ND SD WY; WY: SD NE CO; CO: NE KA OK NM; NM: OK TX AZ;
                         ND: MN SD; SD: MN IA NE; NE: IA MO KA; KA: MO OK; OK: MO AR TX;
                         TX: AR LA; MN: WI IA; IA: WI IL MO; MO: IL KY TN AR; AR: MS TN LA;
                         LA: MS; WI: MI IL; IL: IN KY; IN: OH KY; MS: TN AL; AL: TN GA FL;
                         MI: OH IN; OH: PA WV KY; KY: WV VA TN; TN: VA NC GA; GA: NC SC FL;
                         PA: NY NJ DE MD WV; WV: MD VA; VA: MD DC NC; NC: SC; NY: VT MA CT NJ;
                         NJ: DE; DE: MD; MD: DC; VT: NH MA; MA: NH RI CT; CT: RI; ME: NH;
                         HI: ; AK: """)
print(backtracking_search(a7))


