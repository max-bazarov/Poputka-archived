# Описание моделей

## User
- id
- email
- number
- password
- name
- surname
- age
- passport
- cars (M2M UserCar)

## Ride
- id
- driver (FK User)
- car (FK Car)
- passengers (M2M RidePassenger)
- destination
- departure_point
- time

## RidePassenger
- id
- ride (FK Ride)
- passenger (FK User)

## Booking
- id
- ride (FK Ride)
- user (FK User)
- time

## Car
- id
- make
- model
- year
- license_plate_number
- owner (FK UserCar)

## UserCar
- id
- user (FK User)
- car (FK Car)

## Comment
- id
- author (FK User)
- receiver (FK User)

## Payment
- id
- time
- ride (FK Ride)

## Notification