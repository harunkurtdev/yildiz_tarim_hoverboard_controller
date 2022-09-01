# yildiz_tarim_hoverboard_controller
you control with this package mavros and hoverbord-driver with ros hoverboard-driver ,mavros and joy controller package 

you download your workspace [hoverboard-driver](https://github.com/alex-makarov/hoverboard-driver) and mavros for pixhawk or ardupilot

```mermaid
graph LR
K[Joy] --joy_axes--> D{hoverboard_controller}
A[mavros] --pixhawk or apm mavros servo pinout--> D
D --> E((hoverboard_driver))
```


![hoverboard_image](https://raw.githubusercontent.com/NiklasFauth/hoverboard-firmware-hack/master/pinout.png)


![hoverboard_4_image](https://beta.ivc.no/wiki/images/thumb/2/2d/Bobby_car_hoverboard_upgrade_overview.png/600px-Bobby_car_hoverboard_upgrade_overview.png)
