export interface Pool {
    id: number,
    name: string,
    description: string,
    address: string,
    covered: boolean,
    imageUrl: string
}

export const pools: Pool[] = [
    {
        id: 0,
        name: "Aquapark Kohoutovice",
        description: "Jediný aquapark v Brně",
        address: "Aquapark Kohoutovice, Libušina třída, Kohoutovice, Brno, okres Brno-město, Jihomoravský kraj, Jihovýchod, 623 00, Česko",
        covered: true,
        imageUrl: "https://aquapark.starez.cz/_files/gallery/galerie4/galerie-0393.jpg"

    },
    {
        id: 1,
        name: "Bazény Lužánky",
        description: "2 bazény a wellness v jednom",
        address: "Bazény Lužánky, Sportovní, Ponava, Brno, okres Brno-město, Jihomoravský kraj, Jihovýchod, 601 87, Česko",
        covered: true,
        imageUrl: "https://bazenyluzanky.starez.cz/_files/gallery/galerie3/galerie-1085.jpg"
    },
    {
        id: 2,
        name: "Bazén Ponávka",
        description: "Relaxační i kondiční plavání",
        address: "Bazén Ponávka, Ponávka, Zábrdovice, Brno, okres Brno-město, Jihomoravský kraj, Jihovýchod, 601 51, Česko",
        covered: true,
        imageUrl: "https://ponavka.starez.cz/_files/gallery/galerie9/galerie-0536.jpg"
    },
    {
        id: 3,
        name: "Koupaliště Riviéra",
        description: "Největší brněnské koupaliště",
        address: "Riviéra, Křížkovského, Pisárky, Brno, okres Brno-město, Jihomoravský kraj, Jihovýchod, 603 73, Česko",
        covered: false,
        imageUrl: "https://riviera.starez.cz/_files/gallery/galerie2/galerie-0232.jpg"
    },
    {
        id: 4,
        name: "Koupaliště Zábrdovice",
        description: "Jediné koupaliště v Brně s vlnobitím",
        address: "Zábrdovická 158/13, 615 00 Brno - Zábrdovice, okres Brno-město, Česko",
        covered: false,
        imageUrl: "https://zabrdovice.starez.cz/_files/gallery/galerie8/galerie-0299.jpg"
    }
];

export function getPoolById(id: number): Pool | undefined {
    return pools.find(pool => pool.id == id);
}
