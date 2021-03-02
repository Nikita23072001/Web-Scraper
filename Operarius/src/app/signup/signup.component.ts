import { Component, OnInit } from '@angular/core';
import { AuthService } from '../shared/services/auth.service';
@Component({
selector: 'app-sign-up',
templateUrl: './signup.component.html',
styleUrls: ['./signup.component.css']

})
export class SignUpComponent implements OnInit {
constructor(
public authService: AuthService
) { }
ngOnInit() { }
}
