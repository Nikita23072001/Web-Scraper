import { AuthService } from './../services/auth.service';
import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { AngularFireAuth } from 'angularfire2/auth';
@Injectable({
providedIn: 'root'
})
export class SecureInnerPagesGuard implements CanActivate {
constructor(
    private afAuth: AngularFireAuth,
    public authService: AuthService,
    public router: Router
) { }
canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {
    if (this.authService.isLoggedIn) {
    window.alert('You are not allowed to access this URL!');
    this.router.navigate(['dashboard']);
    }
    return true;
    }
}
