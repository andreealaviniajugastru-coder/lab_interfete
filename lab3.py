#  #ex 1
# picture = [
#  [0,0,0,1,0,0,0],
#  [0,0,1,1,1,0,0],
#  [0,1,1,1,1,1,0],
#  [1,1,1,1,1,1,1],
#  [0,0,0,1,0,0,0],
#  [0,0,0,1,0,0,0]]
# for row in picture:
#      for x in row:
#           if x  ==1:
#               print("*", end="")
#           else:
#               print(" ", end="")
#      print()
#
# #ex2
# # while True:
# #     nota=float(input("introdu nota (1-10): "))
# #     if nota < 1 or nota > 10:
# #         print("nota invalida")
# #         continue
# #     if 9 <= nota <= 10:
# #         print("excelent")
# #     elif 7<= nota <=8:
# #         print("bine")
# #     elif 5 <= nota <=6:
# #         print("suficient")
# #     else:
# #         print("reexaminare")
# #     break
#
# #ex3
# import random
# numar= random.randint(1,50)
# while True:
#      guess = int(input("ghiceste nr(1-50: "))
#      if guess < numar:
#          print("nr este mai mare")
#      elif guess > numar:
#          print("nr este mai mic")
#      else:
#          print("felicitari! ai ghicit")
#          break
#
# #ex4
# print("exercitiul 4")
#
# orase = ["București", "Cluj-Napoca", "Timișoara", "Iași"]
# for index, oras in enumerate(orase, start=1):
#     print(f"{index}. {oras}")
#
#     print("exercitiul 5")
#
#
#     import random
#
#     print("Bine ai venit la Loteria Python!")
#     print("Alege 6 numere între 1 și 49.")
#
#     numere_utilizator = []
#     for i in range(1, 7):
#         n = int(input(f"Numărul {i}: "))
#         numere_utilizator.append(n)
#
#     numere_extrase = random.sample(range(1, 50), 6)
#     ghicite = [n for n in numere_utilizator if n in numere_extrase]
#
#     print(f"Numere extrase: {numere_extrase}")
#     print(f"Ai ghicit {len(ghicite)} numere: {ghicite}")
#
#     if len(ghicite) == 6:
#         print("Felicitări! Ai câștigat marele premiu!")
#     elif len(ghicite) >= 3:
#         print("Felicitări! Ai câștigat un premiu mic!")
#     else:
#         print("Succes data viitoare!")
#
#         print("exercitiul 7")
#
#         comentariu = input("Introdu comentariul tău: ").lower()
#
#         pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
#         negative = ["urat", "prost", "groaznic", "dezamagitor"]
#
#         este_pozitiv = any(cuvant in comentariu for cuvant in pozitive)
#         este_negativ = any(cuvant in comentariu for cuvant in negative)
#
#         if este_pozitiv:
#             print("Comentariu pozitiv!")
#         elif este_negativ:
#             print("Comentariu negativ!")
#         else:
#             print("Comentariu neutru.")
#
#             # Exercițiul 6
#
#             print("Aventura în pădurea magică începe!")
#
#             inventar = []
#
#             alegere = input("Alegi stânga sau dreapta? ").lower()
#
#             if alegere == "stanga":
#                 print("Ai întâlnit un lup!")
#                 actiune = input("Fugi sau lupți? ").lower()
#
#                 if actiune == "fugi":
#                     print("Ai scăpat cu viață!")
#                 else:
#                     print("Ai învins lupul și ai găsit o sabie!")
#                     inventar.append("sabie")
#
#             elif alegere == "dreapta":
#                 print("Ai găsit o comoară!")
#                 inventar.append("aur")
#
#                 actiune = input("Continui sau te întorci? ").lower()

# Exercițiul 8 - Detectare tranzacții suspecte

# tari_risc = ["Coreea de Nord", "Siria", "Iran"]
#
# def verifica_tranzactie(suma, tara, tranzactii_pe_minut):
#     if suma > 10000:
#         return "Suspectă (sumă mare)"
#     elif tara in tari_risc:
#         return "Frauduloasă (țară cu risc ridicat)"
#     elif tranzactii_pe_minut > 3:
#         return "Suspectă (activitate tip bot)"
#     else:
#         return "Sigură"
#
#
# def main():
#     print("=== Sistem detectare tranzacții ===")
#
#     n = int(input("Câte tranzacții vrei să introduci? "))
#
#     tranzactii_suspecte = 0
#
#     for i in range(n):
#         print(f"\nTranzacția {i+1}:")
#
#         suma = float(input("Suma (RON): "))
#         tara = input("Țara: ")
#         tranzactii_pe_minut = int(input("Nr. tranzacții/minut: "))
#
#         rezultat = verifica_tranzactie(suma, tara, tranzactii_pe_minut)
#
#         print(f"→ Tranzacție: {suma} RON din {tara} → {rezultat}")
#
#         if "Suspectă" in rezultat or "Frauduloasă" in rezultat:
#             tranzactii_suspecte += 1
#
#     print(f"\nTotal tranzacții suspecte: {tranzactii_suspecte}")
#
#     if tranzactii_suspecte >= 3:
#         print("⚠️ Cont blocat!")
#     else:
#         print("Cont în siguranță.")
#
#
# if __name__ == "__main__":
#     main()