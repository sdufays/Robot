package layout;
/*
 * BorderLayoutDemo.java
 *
 */
import javax.swing.*;
import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.*;
import java.awt.event.*;


public abstract class BorderLayoutDemo implements ActionListener {
    public static boolean RIGHT_TO_LEFT = false;

    public static void addComponentsToPane(Container pane) {

        if (!(pane.getLayout() instanceof BorderLayout)) {
            pane.add(new JLabel("Container doesn't use BorderLayout!"));
            return;
        }

        if (RIGHT_TO_LEFT) {
            pane.setComponentOrientation(
                    java.awt.ComponentOrientation.RIGHT_TO_LEFT);
        }

        JButton button = new JButton("Stop");
        pane.add(button, BorderLayout.PAGE_START);
        // JButton button = new Jbutton("Forward");
        // pane.add(button, BorderLayout.PAGE_START);

        //Make the center component big, since that's the
        //typical usage of BorderLayout.
        JButton buttonf = new JButton("Forward");
        buttonf.setPreferredSize(new Dimension(100, 200));
        pane.add(buttonf, BorderLayout.CENTER);
        buttonf.addActionListener(this);
        public void actionPerformed(ActionEvent e)
        {
          // TODO import client.java;
          // client.forward();
        }


        JButton buttonl = new JButton("Left");
        buttonl.setPreferredSize(new Dimension(100,200));
        pane.add(buttonl, BorderLayout.LINE_START);

        JButton buttonrv = new JButton("Reverse");
        buttonrv.setPreferredSize(new Dimension(300,100));
        pane.add(buttonrv, BorderLayout.PAGE_END);

        JButton buttonr = new JButton("Right");
        buttonr.setPreferredSize(new Dimension(100,200));
        pane.add(buttonr, BorderLayout.LINE_END);
    }

    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event dispatch thread.
     */
    private static void createAndShowGUI() {

        //Create and set up the window.
        JFrame frame = new JFrame("SCRUMptious Java Client");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //Set up the content pane.
        addComponentsToPane(frame.getContentPane());
        //Use the content pane's default BorderLayout. No need for
        //setLayout(new BorderLayout());
        //Display the window.
        frame.pack();
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        /* Use an appropriate Look and Feel */
        try {
            //UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
            UIManager.setLookAndFeel("javax.swing.plaf.metal.MetalLookAndFeel");
        } catch (UnsupportedLookAndFeelException ex) {
            ex.printStackTrace();
        } catch (IllegalAccessException ex) {
            ex.printStackTrace();
        } catch (InstantiationException ex) {
            ex.printStackTrace();
        } catch (ClassNotFoundException ex) {
            ex.printStackTrace();
        }
        /* Turn off metal's use bold fonts */
        UIManager.put("swing.boldMetal", Boolean.FALSE);

        //Schedule a job for the event dispatch thread:
        //creating and showing this application's GUI.
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
}