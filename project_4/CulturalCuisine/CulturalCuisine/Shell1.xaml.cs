using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using CulturalCuisine.Presenters;

namespace CulturalCuisine
{
    /// <summary>
    /// Interaction logic for Shell1.xaml
    /// </summary>
    public partial class Shell1 : Window
    {
        private ApplicationPresenter _appControl;
        public Shell1()
        {
            InitializeComponent();
            _appControl = new ApplicationPresenter(this);
        }

        private void Button1_Trigger(object sender, RoutedEventArgs e)
        {
            _appControl.button1Toggle();
            Keyboard.Focus(DefFocus);
        }

        private void Button2_Trigger(object sender, RoutedEventArgs e)
        {
            _appControl.button2Toggle();
            Keyboard.Focus(DefFocus);
        }

        private void Button3_Trigger(object sender, RoutedEventArgs e)
        {
            _appControl.button3Toggle();
            Keyboard.Focus(DefFocus);
        }

    }
}
