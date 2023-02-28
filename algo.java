/*
Uses a bactracking approach to solve the 
Cryptarithmetic problem.
 */
import java.util.*;
public class cryparith {
    static boolean flag = false;
    public static int makenum(HashMap<Character,Integer> map,String str){
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<str.length();i++){
            sb.append(map.get(str.charAt(i)));
        }
        String num = sb.toString();
        return (Integer.parseInt(num));
    }
    public static void helper(HashMap<Character,Integer> map,String unique,boolean[] used,String[] words,String result,int target){
        //base case
        if(target==unique.length()){
            int sum = 0;
            for(int i=0;i<words.length;i++){
                sum = sum + makenum(map,words[i]);
            }
            int res = makenum(map,result);
            if(sum==res){
                System.out.println(map);
            }
            return;
        }
        char ch = unique.charAt(target);
        for(int i=0;i<=9;i++){
            if(used[i]==false){
                map.put(ch,i);
                used[i] = true;
                helper(map,unique,used,words,result,target+1);
                //bactracking step (undo changes)
                used[i] = false;
            }
        }
    }
    public static boolean isSolvable(String[] words, String result) {
        HashMap<Character,Integer> map = new HashMap<>();
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<words.length;i++){
            for(int j=0;j<words[i].length();j++){
                char ch = words[i].charAt(j);
                if(map.containsKey(ch)==false){
                    map.put(ch,-1);
                    sb.append(ch);
                }
            }
        }
        for(int i=0;i<result.length();i++){
            char ch = result.charAt(i);
            if(map.containsKey(ch)==false){
                    map.put(ch,-1);
                    sb.append(ch);
                }
        }
        String unique = sb.toString();
        System.out.println("Unique: "+unique);
        boolean used[] = new boolean[10];
        helper(map,unique,used,words,result,0);
        return flag;
    }
    public static void main(String[] args) {
        String words[] = {"SEND","MORE"};
        String res = "MONEY";
        isSolvable(words, res);
    }
}
