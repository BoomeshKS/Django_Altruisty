from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import StudentReport  # Assuming you have a model named StudentReport
from django.views.decorators.csrf import csrf_exempt
import json

strength = []
weakness = []
opportunity = []
threat = []

def createswot(request):
    latest_report = StudentReport.objects.filter(student_id='1234567891').order_by('-timestamp').first()

    context = {
        'strength': latest_report.strengths,
        'weakness': latest_report.weakness,
        'opportunity': latest_report.opportunity,
        'threat': latest_report.threat,
        'new': 'no'
    }

    return render(request, 'swot_analysis/points.html', context)

def strength(request):
    return render(request, 'swot_analysis/strength.html')

def report_detail(request, id):
    report = get_object_or_404(StudentReport, id=id)
    return render(request, 'swot_analysis/viewswot.html', {'report': report})

def viewImprovement(request, id):
    report = get_object_or_404(StudentReport, id=id)
    improvements = report.improvements
    addons = report.addons

    return render(request, 'swot_analysis/viewimprovements.html', {
        'report': report,
        'improvements': improvements,
        'addons': addons
    })

def swotStartNow(request):
    student_id = "1234567891"
    report_count = StudentReport.objects.filter(student_id=student_id).count()

    if report_count == 0:
        return render(request, 'swot_analysis/swot.html')

    elif report_count >= 1:
        search_query = request.GET.get('q', '')

        if search_query:
            reports = StudentReport.objects.filter(student_id=student_id, title__icontains=search_query)
        else:
            reports = StudentReport.objects.filter(student_id=student_id)

        print(f"Reports found: {reports}")

        return render(request, 'swot_analysis/list.html', {'reports': reports, 'search_query': search_query})

@csrf_exempt
def delete_report(request, report_id):
    if request.method == 'POST':
        report = StudentReport.objects.get(id=report_id)
        report.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def swot(request):
    return render(request, 'swot_analysis/swot.html')

def points(request, data):
    report_count = 0
    if report_count >= 1:
        return render(request, 'swot_analysis/points.html', {"new": "no", "strength": strength, "weakness": weakness, "oppor": opportunity, "threat": threat})
    else:
        student_id = '1234567891'
        objecdata = data
        objedata = objecdata.replace("--", ":")
        objectdata = objedata.replace("-", " ")
        realdata = objectdata.split(",,")
        strength_raw = realdata[0].split(":")
        strength = strength_raw[1].split(",")
        weakness_raw = realdata[1].split(":")
        weakness = weakness_raw[1].split(",")
        opportunity_raw = realdata[2].split(":")
        opportunity = opportunity_raw[1].split(",")
        threat_raw = realdata[3].split(":")
        threat = threat_raw[1].split(",")

        title = 'First analysis'
        savedata = StudentReport(student_id=student_id, title=title, strengths=strength, weakness=weakness, opportunity=opportunity, threat=threat)
        savedata.save()

        return redirect('swot-start-now')

def list(request):
    return render(request, 'swot_analysis/list.html')

def overview(request):
    return render(request, 'swot_analysis/overview.html')

def improvement(request):
    # Filter entries by student_id and order by timestamp
    reports = StudentReport.objects.filter(student_id="1234567891").order_by('-timestamp')[:2]
    
    # Initialize an empty dictionary for combined SWOT categories
    combined_swot = {"strength": [], "weakness": [], "opportunity": [], "threat": []}

    if len(reports) >= 2:
        # Define latest and second latest reports
        latest_report = reports[0]
        second_latest_report = reports[1]
        
        # Categories to be compared
        categories = ["strengths", "weakness", "opportunity", "threat"]
        
        for category in categories:
            # Get the list of points in each category for both latest and second latest reports
            latest_points = latest_report.__dict__.get(category, [])
            second_latest_points = second_latest_report.__dict__.get(category, [])
            
            # Identify extra points in the latest report that aren't in the second latest
            extra_points = []
            for point in latest_points:
                if point not in second_latest_points:
                    extra_points.append(point)
            
            # Assign the list of extra points to the combined_swot dictionary
            combined_swot[category] = extra_points
    
    return render(request, 'swot_analysis/improve.html', {'combined_swot': combined_swot})

def save_improvements(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            improvements = data.get('improvements', [])
            addons = data.get('addons', {})
            report = StudentReport.objects.filter(student_id='1234567891').latest('timestamp')
            report.improvements = improvements
            report.addons = addons
            report.save()

            return JsonResponse({'success': True, 'message': 'Improvements saved successfully.'})

        except StudentReport.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Report not found for this student.'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)

def index(request):
    return render(request, 'index.html')

def save_swot_analysis(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        strengths = request.POST.get('strengths')
        weakness = request.POST.get('weakness')
        opportunity = request.POST.get('opportunity')
        threat = request.POST.get('threat')

        strengths_list = [s.strip() for s in strengths.split(',')]
        weakness_list = [w.strip() for w in weakness.split(',')]
        opportunity_list = [o.strip() for o in opportunity.split(',')]
        threat_list = [t.strip() for t in threat.split(',')]

        student_report = StudentReport(
            student_id='1234567891',
            title=title,
            timestamp=timezone.now(),
            strengths=strengths_list,
            weakness=weakness_list,
            opportunity=opportunity_list,
            threat=threat_list,
            improvements=None,
            addons=None
        )
        student_report.save()

        return redirect('improvement')

    return render(request, 'swot_analysis/points.html')
