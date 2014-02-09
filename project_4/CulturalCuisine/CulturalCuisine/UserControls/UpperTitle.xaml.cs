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

namespace CulturalCuisine.UserControls
{
    /// <summary>
    /// Interaction logic for UpperTitle.xaml
    /// </summary>
    public partial class UpperTitle : UserControl
    {
        private ApplicationPresenter _appControl;

        public UpperTitle(ApplicationPresenter appControl)
        {
            InitializeComponent();
            _appControl = appControl;
        }

        private void Button1_Trigger(object sender, RoutedEventArgs e)
        {
            System.Diagnostics.Debug.Write("Button press 1\n");
            _appControl.button1Toggle();
            System.Diagnostics.Debug.Write("Button Toggle called 1\n");
            Keyboard.Focus(DefFocus);
        }

        private void Button2_Trigger(object sender, RoutedEventArgs e)
        {
            System.Diagnostics.Debug.Write("Button press 2\n");
            _appControl.button2Toggle();
            System.Diagnostics.Debug.Write("Button Toggle called 2\n");
            Keyboard.Focus(DefFocus);
        }

        private void Button3_Trigger(object sender, RoutedEventArgs e)
        {
            System.Diagnostics.Debug.Write("Button press 3\n");
            _appControl.button3Toggle();
            System.Diagnostics.Debug.Write("Button Toggle called 3\n");
            Keyboard.Focus(DefFocus);
        }
    }
}
