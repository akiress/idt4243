using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using CulturalCuisine.UserControls;
using System.Windows.Media;

namespace CulturalCuisine.Presenters
{
    public class ApplicationPresenter
    {
        private Shell1 _shell1;
        private Shell2 _shell2;
        private TitleUC _titleUC;
        private UpperTitle _upperTitleUC;

        private bool _button1State;
        private bool _button2State;
        private bool _button3State;
        private int _buttonCount;

        private UC1Scr _uc1Scr;
        private UC2Scr _uc2Scr;
        private UC3Scr _uc3Scr;

        private HistoryUC _histUC;
        private NutritionUC _nutUC;
        private RecipeUC _recUC;

        public ApplicationPresenter(Shell1 shell)
        {
            _shell1 = shell;
            _shell2 = new Shell2(this);
            _titleUC = new TitleUC();
            _upperTitleUC = new UpperTitle(this);
            _shell2.Shell2Viewport.Content = _upperTitleUC;
            _shell2.Show();
            _shell1.Shell1ViewPort.Content = _titleUC;

            _button1State = false;
            _button2State = false;
            _button3State = false;
            _buttonCount = 0;

            _uc1Scr = new UC1Scr(this);
            _uc2Scr = new UC2Scr(this);
            _uc3Scr = new UC3Scr(this);

            _histUC = new HistoryUC(this);
            _nutUC = new NutritionUC(this);
            _recUC = new RecipeUC(this);
        }

        public void button1Toggle()
        {
            if (_button1State)
            {
                _button1State = false;
                _shell1.Button1.Background = Brushes.LightPink;
                _buttonCount--;
            }
            else
            {
                _button1State = true;
                _shell1.Button1.Background = Brushes.LightGreen;
                _buttonCount++;
            }

            dataViewUpdate();
        }

        public void button2Toggle()
        {
            if (_button2State)
            {
                _button2State = false;
                _shell1.Button2.Background = Brushes.LightPink;
                _buttonCount--;
            }
            else
            {
                _button2State = true;
                _shell1.Button2.Background = Brushes.LightGreen;
                _buttonCount++;
            }

            dataViewUpdate();
        }

        public void button3Toggle()
        {
            if (_button3State)
            {
                _button3State = false;
                _shell1.Button3.Background = Brushes.LightPink;
                _buttonCount--;
            }
            else
            {
                _button3State = true;
                _shell1.Button3.Background = Brushes.LightGreen;
                _buttonCount++;
            }

            dataViewUpdate();
        }

        public void dataViewUpdate()
        {
            if (_buttonCount == 1)
            {
                _shell2.Shell2Viewport.Content = _uc1Scr;
                set1ScrView();
            }
            else if (_buttonCount == 2)
            {
                _shell2.Shell2Viewport.Content = _uc2Scr;
                set2ScrView();
            }
            else if (_buttonCount == 3)
            {
                _shell2.Shell2Viewport.Content = _uc3Scr;
                set3ScrView();
            }
            else
            {
                _shell2.Shell2Viewport.Content = _upperTitleUC;
            }
        }

        public void set1ScrView()
        {
            clearUCScontent();
            if (_button1State)
            {
                _uc1Scr.UC1ScrView1.Content = _histUC;
            }
            else if (_button2State)
            {
                _uc1Scr.UC1ScrView1.Content = _nutUC;
            }
            else if (_button3State)
            {
                _uc1Scr.UC1ScrView1.Content = _recUC;
            }
            else
            {
                _uc1Scr.UC1ScrView1.Content = _titleUC;
            }
        }

        public void set2ScrView()
        {
            clearUCScontent();
            if (_button1State)
            {
                _uc2Scr.UC2ScrView1.Content = _histUC;
                if (_button2State)
                {
                    _uc2Scr.UC2ScrView2.Content = _nutUC;
                }
                else if (_button3State)
                {
                    _uc2Scr.UC2ScrView2.Content = _recUC;
                }
                else
                {
                }
            }
            else if (_button2State)
            {
                _uc2Scr.UC2ScrView1.Content = _nutUC;
                _uc2Scr.UC2ScrView2.Content = _recUC;
            }
            else
            {
                _uc2Scr.UC2ScrView1.Content = _titleUC;
                _uc2Scr.UC2ScrView2.Content = _titleUC;
            }
        }

        public void set3ScrView()
        {
            clearUCScontent();
            _uc3Scr.UC3ScrView1.Content = _histUC;
            _uc3Scr.UC3ScrView2.Content = _nutUC;
            _uc3Scr.UC3ScrView3.Content = _recUC;
        }

        public void clearUCScontent()
        {
            _uc1Scr.UC1ScrView1.Content = null;
            _uc2Scr.UC2ScrView1.Content = null;
            _uc2Scr.UC2ScrView2.Content = null;
            _uc3Scr.UC3ScrView1.Content = null;
            _uc3Scr.UC3ScrView2.Content = null;
            _uc3Scr.UC3ScrView3.Content = null;
        }
    }
}
