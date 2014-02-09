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
using System.Windows.Shapes;
using CulturalCuisine.Presenters;

namespace CulturalCuisine
{
    /// <summary>
    /// Interaction logic for Shell2.xaml
    /// </summary>
    public partial class Shell2 : Window
    {
        private ApplicationPresenter _appControl;
        public Shell2(ApplicationPresenter appControl)
        {
            InitializeComponent();
            _appControl = appControl;

        }
    }
}
