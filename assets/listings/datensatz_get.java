public String get(Attribut a) {
    switch (a) {
    case Alter:
        return Alter;
    case Aufzug:
        return Aufzug;
    // ...
    case Bewertung:
        return Bewertung ?
                Konstanten.wahr :
                Konstanten.falsch;
    }
    throw new RuntimeException("Wrong Type");
}