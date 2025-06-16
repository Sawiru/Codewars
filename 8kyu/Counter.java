/*Consider an array/list of sheep where some sheep may be missing from their place. We need a 
function that counts the number of sheep present in the array (true means present). */

public class Counter {
    public static int countSheeps(Boolean[] arrayOfSheeps) {
      int counter = 0;
      
      for (Boolean sheeps : arrayOfSheeps) {
        if (Boolean.TRUE.equals(sheeps)) {
          counter ++;
        }
      }
      
      return counter;
      
    }
}
