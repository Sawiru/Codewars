/*Description
We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.*/

public class StringToNumber {
  public static int stringToNumber(String str) {
    //TODO: Convert str into a number
    int number = Integer.parseInt(str);
    return number;    
  }
}
