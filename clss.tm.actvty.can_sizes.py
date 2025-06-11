'''
Can Sizes Team Activity
Last Updated: 05/20/25
Author: Michael Jacob (MJ) Quizon
'''
import math

def main():
    name = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303']
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    volume = []
    surface_area = []
    storage_efficiency = []
    for radi, heights in zip(radius, height):
        calculated_volume = compute_volume(radi, heights)
        volume.append(calculated_volume)
        calculated_surface_area = compute_surface_area(radi, heights)
        surface_area.append(calculated_surface_area)
    #
    for volumes, surface_areas in zip(volume, surface_area):
        calculated_storage_efficiency = compute_storage_efficiency(volumes, surface_areas)
        storage_efficiency.append(calculated_storage_efficiency)
    #
    for names, storage_efficiencies in zip(name, storage_efficiency):
        print(f'{names} {storage_efficiencies:.2f}')

def compute_volume(radi, heights):
    calculated_volume = math.pi * (radi**2) * heights
    return calculated_volume

def compute_surface_area(radi, heights):
    calculated_surface_area = 2*math.pi*radi*(radi+heights)
    return calculated_surface_area

def compute_storage_efficiency(volumes, surface_areas):
    calculated_storage_efficiency = volumes/surface_areas
    return calculated_storage_efficiency

main()