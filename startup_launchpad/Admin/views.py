from django.shortcuts import render

def CourseListAdmin(request):
    return render(request, 'Admin/Courses/course-list-admin.html')

def view_students(request):
    
    return render(request, 'Admin/Courses/view-students.html')

def view_startup(request):
    
    return render(request, 'Admin/Courses/view-startup.html')
