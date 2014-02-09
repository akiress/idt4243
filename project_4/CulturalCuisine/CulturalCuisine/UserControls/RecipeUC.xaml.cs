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
    /// Interaction logic for RecipeUC.xaml
    /// </summary>
    public partial class RecipeUC : UserControl
    {

        private ApplicationPresenter _appControl;

        public RecipeUC(ApplicationPresenter appControl)
        {
            InitializeComponent();
            _appControl = appControl;
        }
    }
}
