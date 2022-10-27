import java.util.*;

public class BST_Strings {
    static class Node{
        Node left;
        Node right;
        String data;
        Node(String data){
            this.data=data;
            this.left=null;
            this.right = null;
        }
    }

    public static Node bst_insert_recur(Node root,String value){
        if(root==null){
            return new Node(value);
        }
        if(value.compareToIgnoreCase(root.data)<0) {
            root.left= bst_insert_recur(root.left,value);
        }
        else{
            root.right = bst_insert_recur(root.right,value);
        }
        return root;
    }
    public static Node bst_insert_nonrecur(Node root,String value){
        Node x = root;
        Node y = null;
        if(root==null){
            return new Node(value);
        }
        while (x!=null){
            y=x;
            if(value.compareToIgnoreCase(x.data)<0){x=x.left;}
            else{x=x.right;}
        }
        if(value.compareToIgnoreCase(y.data)<0){y.left=new Node(value);}
        else{y.right=new Node(value);}
        return root;
    }

    public static boolean bst_search(Node root,String value){
        if(root==null){
            return false;
        }
        else{
            if(value.compareToIgnoreCase(root.data)==0){
                return true;
            }
            if(value.compareToIgnoreCase(root.data)<0){
                return bst_search(root.left,value);
            }
            else{
                return bst_search(root.right,value);
            }
        }
    }

    public static boolean bst_search_nonrecur(Node root,String value){
        if(root==null){
            return false;
        }
        else{
            while (root!=null){
                if(value.compareToIgnoreCase(root.data)==0){
                    return true;
                }
                else if(value.compareToIgnoreCase(root.data)<0){
                    root = root.left;
                }
                else{
                    root = root.right;
                }
            }
        }
        return false;
    }

    public static void Inorder(Node root){
        if(root==null){
            return;
        }
        Inorder(root.left);
        System.out.print(root.data+" ");
        Inorder(root.right);
    }

    public static void main(String[] args) {
        List<String> values = Arrays.asList("Rama","Krishna","Hanuma","Arjuna","Bheema");
        Node root = null;
        for(int i=0;i<values.size();i++){
            root = bst_insert_nonrecur(root,values.get(i));
        }
        System.out.print("Inorder Traversal -> ");
        Inorder(root);
        System.out.println();
        System.out.println(bst_search(root,"Arjuna"));
        System.out.println(bst_search(root,"Arj"));
        System.out.println(bst_search_nonrecur(root,"Hanuma"));
        System.out.println(bst_search_nonrecur(root,"krish"));

    }
}
