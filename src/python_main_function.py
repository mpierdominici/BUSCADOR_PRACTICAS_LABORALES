from practicasLaboralesList import  practicasLaboralesList

def main():
    pl = practicasLaboralesList("../data/db.csv")
    print(pl.listaPracticasLaborales[6].tags[0])

if __name__ == '__main__':
    main()
