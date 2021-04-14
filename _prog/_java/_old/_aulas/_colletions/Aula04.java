import java.util.Arrays;
import java.util.Collections;
import java.util.List;


/**
 * Card
 */
class Card {

    public static enum Face {Ace, Deuce, Three, Four, Five, Six,
        Seven, Eight, Nine, Ten, Jack, Queen, King };

    public static enum Suit {Clubs, Diamonds, Hearts, Spades};

    private final Face face;
    private final Suit suit;

    // construtor
    public Card(Face face, Suit suit) {
        this.face = face;
        this.suit = suit;
    }

    // retorna face da carta
    public Face getFace(){
        return face;
    }

    // retorna naipe de carta
    public Suit getSuit(){
        return suit;
    }

    // retorna representação da carta
    public String toString(){
        return String.format("%s of %s", face, suit);
    }


}


/**
 * Aula04
 */
public class Aula04 {

    private List<Card> list;

    // configura baralho de carta e embarelha
    public Aula04(){
        Card[] deck = new Card[52];
        int cont = 0;

        // preenche objectos com card
        for(Card.Suit suit : Card.Suit.values()){
            for(Card.Face face : Card.Face.values()){
                deck[cont] = new Card(face, suit);
                ++cont;
            }
        }

        list = Arrays.asList(deck); // obtém lista
        Collections.shuffle(list);// embarelha carta
    }

    // gera saída de baralho
    public void printCards(){
        // exibe 52 cartas em 2 calunas
        for(int i = 0; i < list.size(); i++){
            System.out.printf("%-19s%s", list.get(i), ((i + 1) % 4 == 0 ? "\n" : ""));
        }
    }

    public static void main(String[] args) {
        Aula04 card = new Aula04();
        card.printCards();
    }
}