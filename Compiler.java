import java.io.*;
import java.util.*;

public class Compiler {
	public static void main(String[] args) {
		
		// Read from Main.esp

		File myObj = new File("Main.esp");
		String fileContents = "";

		try (Scanner myReader = new Scanner(myObj)) {
      			
			while (myReader.hasNextLine()) {
        			String data = myReader.nextLine();
				fileContents += data + "\n";
      			}

    		} catch (FileNotFoundException e) {
      			System.out.println("An error occurred.");
      			e.printStackTrace();
    		} 

		// Split fileContents into an array of lines

		String[] arrayLines = fileContents.split("\n");

		System.out.println(arrayLines[0]);
	}
}
