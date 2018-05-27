package com.map.demo;

import java.util.Map;

/**
 * Created by lee on 05/04/18.
 * TreeMap实现了SortedMap接口，也就是说会按照key的大小顺序对Map中的元素进行排序，
 * key大小的评判可以通过其本身的自然顺序（natural ordering），也可以通过构造时传入的比较器（Comparator）
 * TreeMap底层通过红黑树（Red-Black tree）实现
 */
public class TreeMapDemo<K,V> {

    private transient Entry<K,V> root;

    // Rotate Left
    private void rotateLeft(Entry<K, V> p) {
        if (p != null) {
            Entry<K, V> r = p.right;
            p.right = r.left;
            if (r.left != null) {
                r.left.parent = p;
            }
            r.parent = p.parent;

            if (p.parent == null) {
                root = r;
            } else if (p.parent.left == p) {
                p.parent.left = r;
            } else {
                p.parent.right = r;
            }
            r.left = p;
            p.parent = r;
        }

    }

    static final class Entry<K,V> implements Map.Entry<K,V> {
        K key;
        V value;
        Entry<K, V> left;
        Entry<K, V> right;
        Entry<K, V> parent;
        /**
         * black
         */
        boolean color = true;

        @Override
        public K getKey() {
            return null;
        }

        @Override
        public V getValue() {
            return null;
        }

        @Override
        public V setValue(V value) {
            return null;
        }
    }

}
