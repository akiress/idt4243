﻿#pragma checksum "..\..\..\..\UserControls\UpperTitle.xaml" "{406ea660-64cf-4c82-b6f0-42d48172a799}" "0E2D918D7C18FC7D9FC6975778E798D2"
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.296
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Markup;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Effects;
using System.Windows.Media.Imaging;
using System.Windows.Media.Media3D;
using System.Windows.Media.TextFormatting;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Shell;


namespace CulturalCuisine.UserControls {
    
    
    /// <summary>
    /// UpperTitle
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "4.0.0.0")]
    public partial class UpperTitle : System.Windows.Controls.UserControl, System.Windows.Markup.IComponentConnector {
        
        
        #line 106 "..\..\..\..\UserControls\UpperTitle.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button Button1;
        
        #line default
        #line hidden
        
        
        #line 108 "..\..\..\..\UserControls\UpperTitle.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button Button2;
        
        #line default
        #line hidden
        
        
        #line 110 "..\..\..\..\UserControls\UpperTitle.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button Button3;
        
        #line default
        #line hidden
        
        
        #line 111 "..\..\..\..\UserControls\UpperTitle.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Control DefFocus;
        
        #line default
        #line hidden
        
        private bool _contentLoaded;
        
        /// <summary>
        /// InitializeComponent
        /// </summary>
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        public void InitializeComponent() {
            if (_contentLoaded) {
                return;
            }
            _contentLoaded = true;
            System.Uri resourceLocater = new System.Uri("/CulturalCuisine;component/usercontrols/uppertitle.xaml", System.UriKind.Relative);
            
            #line 1 "..\..\..\..\UserControls\UpperTitle.xaml"
            System.Windows.Application.LoadComponent(this, resourceLocater);
            
            #line default
            #line hidden
        }
        
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Never)]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Design", "CA1033:InterfaceMethodsShouldBeCallableByChildTypes")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Maintainability", "CA1502:AvoidExcessiveComplexity")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1800:DoNotCastUnnecessarily")]
        void System.Windows.Markup.IComponentConnector.Connect(int connectionId, object target) {
            switch (connectionId)
            {
            case 1:
            this.Button1 = ((System.Windows.Controls.Button)(target));
            
            #line 106 "..\..\..\..\UserControls\UpperTitle.xaml"
            this.Button1.Click += new System.Windows.RoutedEventHandler(this.Button1_Trigger);
            
            #line default
            #line hidden
            return;
            case 2:
            this.Button2 = ((System.Windows.Controls.Button)(target));
            
            #line 108 "..\..\..\..\UserControls\UpperTitle.xaml"
            this.Button2.Click += new System.Windows.RoutedEventHandler(this.Button2_Trigger);
            
            #line default
            #line hidden
            return;
            case 3:
            this.Button3 = ((System.Windows.Controls.Button)(target));
            
            #line 110 "..\..\..\..\UserControls\UpperTitle.xaml"
            this.Button3.Click += new System.Windows.RoutedEventHandler(this.Button3_Trigger);
            
            #line default
            #line hidden
            return;
            case 4:
            this.DefFocus = ((System.Windows.Controls.Control)(target));
            return;
            }
            this._contentLoaded = true;
        }
    }
}

