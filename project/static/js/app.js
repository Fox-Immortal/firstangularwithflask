var myApp = angular.module('myApp', ['ngRoute', 'angularCSS', 'ngAnimate', 'chart.js']);

myApp.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {

  $routeProvider
    .when('/', {
      templateUrl: 'static/partials/login.html',
      controller: 'loginController',
      css: '/static/css/login.css'
    })
    .when('/main', {
      templateUrl: 'static/partials/main.html',
      controller: 'mainController',
      css: '/static/css/main.css'
    })
    .when('/hello', {
      templateUrl: 'static/partials/hi.html'
    })
    .otherwise({
      redirectTo: '/'
    });
  $locationProvider.html5Mode({
    enabled: true,
    requireBase: false,
    rewriteLinks: false

  });
}]);