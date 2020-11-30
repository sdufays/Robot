import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;

public class Main extends JFrame implements ActionListener {
  int index = 0;
  String[] msgs = { "test", "Left", "Right", "Test", "Forward", "Reverse"};
  JButton button1 = new JButton("Left");
  JButton button2 = new JButton("Right");
  JButton button3 = new JButton(msgs[0]);
  JButton button4 = new JButton("Forward");
  JButton button5 = new JButton("Reverse");

  public Main() {
    BorderLayout layout = new BorderLayout();
    setLayout(layout);
    button1.addActionListener(this);
    button2.addActionListener(this);
    button3.setEnabled(false);
    button4.addActionListener(this);
    button5.addActionListener(this);
    add(button1, BorderLayout.WEST);
    add(button2, BorderLayout.EAST);
    add(button3, BorderLayout.CENTER);
    add(button4, BorderLayout.NORTH);
    add(button5, BorderLayout.SOUTH);
    setDefaultCloseOperation(EXIT_ON_CLOSE);
    setSize(400, 200);
    setVisible(true);
  }

  @Override
  public void actionPerformed(ActionEvent e) {
    Object obj = e.getSource();
    if (obj == button1)
    {
      index = 1;
      //TODO connect Client
    }
    else if (obj == button2)
    {
      index = 2;
      //TODO connect Client
    }
    else if (obj == button4)
    {
      index = 4;
      //TODO connect Client
    }
    else if (obj == button5)
    {
      index = 5;
      //TODO connect Client
    }
    button3.setText(msgs[index]);
  }

  public static void main(String[] args) {
    Main app = new Main();

  }

}
