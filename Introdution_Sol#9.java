import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = 0;
        String line;
        while(sc.hasNext()){
        line = sc.nextLine();
        System.out.println(++i + " " + line);
        }
    }
}